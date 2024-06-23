import httpx
import asyncio
import inspect
import time
import json
import hashlib
from .utils.firebase import upload_text_to_firebase, upload_data_to_firebase, download_file, download_json_file
from .utils.display_util import clear_line, green_check, red_check, reset_color
import time
import urllib.parse
from .utils.source_code import get_source_code_hash

BASE_URL="http://localhost:8080"
BASE_CLIENT_URL="http://localhost:3000"
# BASE_URL="https://lyraml-api-2-7c3apmua4a-uc.a.run.app"
PROJECT_BASE_URL = BASE_URL + "/projects"
RUN_BASE_URL = BASE_URL + "/runs"
DATASET_BASE_URL = BASE_URL + "/datasets"
JUDGE_BASE_URL = BASE_URL + "/judges"
EVALUATION_BASE_URL = BASE_URL + "/evaluations"

async def post_data(url, json_data):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=json_data)
        return response


async def get_data(url):
    async with httpx.AsyncClient() as client: 
        response = await client.get(url)
        return response

def print_error_message(code):
    try:
        print(error_code_message_map[code])
    except:
        print(error_code_message_map['unexpected_error'])

error_code_message_map = {
    'invalid_api_key': 'Invalid API Key. Please verify your API Key or generate a new one at https://lyra-ml.com Workspace Settings tab.',
    'exceed_storage_limit': '🚧 You\'ve reached your storage limit! To keep everything running smoothly, please visit our Pricing Page to explore upgrade options that suit your needs.',
    'unexpected_error': 'Oops! Something went wrong on our end. Please try again later. If the issue persists, feel free to contact our support team. We\’re here to help!'
}

class Lyra:
    def __init__(self, project_name, API_KEY):
        self.projectId = None
        self.error_code = None
        self.judges = []
        response = asyncio.run(post_data(PROJECT_BASE_URL, json_data={'project_name': project_name, 'api_key': API_KEY}))
        if response.status_code == 201:
            body = json.loads(response.text)
            self.projectId = body["project"]["id"]
        else:
            body = json.loads(response.text)
            self.error_code = body["code"]
            print_error_message(self.error_code)

    def _download_dataset(self, dataset_tag):
        response = asyncio.run(get_data(DATASET_BASE_URL + "/" + dataset_tag))
        body = json.loads(response.text)
        dataset_url = body["dataset"]["url"]
        dataset = download_json_file(dataset_url)
        return dataset

    def upload_dataset(self, dataset):
        serialized_dataset = json.dumps(dataset.to_json()).encode('utf-8')
        hasher = hashlib.sha256()
        hasher.update(serialized_dataset)
        hash_digest = hasher.hexdigest()
        public_url, data_size = upload_data_to_firebase(serialized_dataset, hash_digest + '_dataset.txt')
        response = asyncio.run(post_data(DATASET_BASE_URL, json_data={
            'projectId': self.projectId,
            'name': dataset.name,
            'url': public_url,
            'dataSize': data_size,
            'codeHash': hash_digest,
        }))
        body = json.loads(response.text)
        tag = body["tag"]
        return tag

    def add_judge(self, judge):
        # Grab the source code and hash of scoring_rubric and passing_criteria
        scoring_source_code, judge_scoring_hash = get_source_code_hash(judge.scoring_rubric)
        passing_criteria_source_code, judge_passing_hash = get_source_code_hash(judge.passing_criteria)
        
        judge_tag_response = asyncio.run(post_data(JUDGE_BASE_URL + "/judgeTag", json_data={
            'name': judge.name,
            'judge_scoring_hash': judge_scoring_hash,
            'judge_passing_hash': judge_passing_hash,
            'projectId': self.projectId,
        }))
        judgeTag = json.loads(judge_tag_response.text)["judgeTag"]

        # Upload scoring source code and passing criteria source code to firebase
        scoring_source_public_url, scoring_source_data_size = upload_text_to_firebase(scoring_source_code, judgeTag + '_scoring.txt')
        passing_public_url, passing_data_size = upload_text_to_firebase(passing_criteria_source_code, judgeTag + '_passing.txt')
        response = asyncio.run(post_data(JUDGE_BASE_URL, json_data={
            'judge': json.dumps(judge.to_json()),
            'projectId': self.projectId,
            'scoring_source_code_url': scoring_source_public_url,
            'scoring_hash': judge_scoring_hash,
            'passing_criteria_code_url': passing_public_url,
            'passing_hash': judge_passing_hash,
            'data_size': scoring_source_data_size + passing_data_size,
            'tag': judgeTag,
        }))
        if response.status_code == 201:
            body = json.loads(response.text)
            if body["isNew"]:
                print(f"✔ Judge {judgeTag} created.")
            else:
                print(f"✔ Judge {judgeTag} already exists.")
            
                for item in body["itemsUpdated"]:
                    print(f"✔ Judge {item['field']} field has been updated to: \"{item['value']}\"")
        
    def _get_judge_from_judge_tag(self, judge_tag):
        encoded_judge_tag = urllib.parse.quote(judge_tag)
        judge_response = asyncio.run(get_data(JUDGE_BASE_URL + "/" + encoded_judge_tag + "/projects/" + self.projectId))
        judge = json.loads(judge_response.text)["judge"]
        return judge

    def _get_scoring_rubric_func_from_judge(self, judge):
        scoring_code_url = judge["scoringSourceCodeUrl"]
        scoring_code_str = download_file(scoring_code_url)
        decoded_scoring_code_str = scoring_code_str.decode('utf-8')
        exec(decoded_scoring_code_str, globals())
        return scoring_rubric


    def evaluate_with(self, judge_tag):
        judge = self._get_judge_from_judge_tag(judge_tag)        

        def decorator(func):
            def wrapper(*args, **kwargs):
                dataset = self._download_dataset(judge["dataset_tag"])
                passed_cases = 0
                failed_cases = 0
                i = 1
                scores = []
                for row in dataset["data"]:
                    message = f"Evaluating {dataset['name']} {i}/{len(dataset['data'])}..."
                    print(f"\n{message}", end="", flush=True)
                    outputs = func(row)
                    scoring_rubric = self._get_scoring_rubric_func_from_judge(judge)
                    score = scoring_rubric(outputs)
                    scores.append({
                        "output": outputs,
                        "score": score,
                    })
                    clear_line()
                    if judge.passing_criteria(outputs):
                        passed_cases += 1
                        print(f"\r{green_check()} {dataset['name']}[{i}] score: {score} {reset_color()}", end="", flush=True)
                    else:
                        failed_cases += 1
                        print(f"\r{red_check()} {dataset['name']}[{i}] score: {score} {reset_color()}", end="", flush=True)
                    i += 1

                if failed_cases == 0:
                    print(f"\n{green_check()} All cases in dataset passed.")
                else:
                    print(f"\n\n{red_check()} {failed_cases} out of {len(dataset['data'])} failed")

                response = asyncio.run(post_data(EVALUATION_BASE_URL, json_data={
                    'scores': scores,
                    'judge_tag': judge["tag"],
                    'projectId': self.projectId,
                }))
                print("evaluation response: ", response)
                return func(*args, **kwargs)
            return wrapper
        return decorator

    # TODO: Modularize this
    def trace(self, func):
        def wrapper(*args, **kwargs):
            if self.error_code:
                return
            # print("args: ", args)
            # print("type(args[0]): ", type(args[0]))
            # print("kwargs: ", kwargs)
            params = inspect.signature(func).parameters
            # print("params: ", params)
            source_code = inspect.getsource(func)
            hasher = hashlib.sha256()
            hasher.update(source_code.encode('utf-8'))
            hash_digest = hasher.hexdigest()
            # print(f"Hash: {hash_digest}")

            start = time.perf_counter()
            result = func(*args, **kwargs)
            latency = time.perf_counter() - start

            # Save the source code to a file
            public_url, data_size = upload_text_to_firebase(source_code, hash_digest + '_code-snippet.txt')

            param_keys = [key for key in params]
            formatted_args = []
            i = 0
            for arg in args:
                formatted_args.append({
                    'name': param_keys[i],
                    'value': arg,
                    'type': type(arg).__name__,
                })
                i += 1 
            
            formatted_outputs = {
                'value': result,
                'type': type(result).__name__,
            }

            response = asyncio.run(post_data(RUN_BASE_URL, json_data={
                'codeSnippetUrl': public_url,
                'latency': latency,
                'projectId': self.projectId,
                'funcName': func.__name__,
                'codeHash': hash_digest,
                'inputs': formatted_args,
                'outputs': formatted_outputs,
                'dataSize': data_size,
            }))

            body = json.loads(response.text)
            if response.status_code == 201:
                print("✨ View run " + body["run"]["id"] + " at " + BASE_CLIENT_URL + "/workspace/" + body["workspaceId"] + "/project/" + self.projectId)
                return result
            else:    
                self.error_code = body["code"]
                print_error_message(self.error_code)

        return wrapper


class Dataset:
    def __init__(self, dataset_name, data):
        self.name = dataset_name
        self.data = data
    
    def to_json(self):
        return {
            "name": self.name,
            "data": self.data
        }


# spinner = spinning_cursor()
# for _ in range(50):  # Adjust the range for duration
#     sys.stdout.write(next(spinner))  # Use sys.stdout.write for faster prints
#     sys.stdout.flush()
#     time.sleep(0.1)  # Adjust as necessary for speed
#     sys.stdout.write('\b')  # Use backspace to erase the last character