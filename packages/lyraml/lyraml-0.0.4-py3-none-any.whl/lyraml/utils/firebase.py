import io
import os
import firebase_admin
from firebase_admin import credentials, storage
import requests
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
# Production configuration: lyraml-firebase-adminsdk-tzq8c-0de38b28e2.json
# file_path = os.path.join(dir_path, "lyraml-firebase-adminsdk-tzq8c-0de38b28e2.json")

# Dev configuration: 
file_path = os.path.join(dir_path, "lyraml-dev-firebase-adminsdk-v4hs3-b945386918.json")
cred = credentials.Certificate(file_path)

# Production configuration: 
# firebase_admin.initialize_app(cred, {
#     'storageBucket': 'lyraml.appspot.com'
# })

# Dev configuration
firebase_admin.initialize_app(cred, {
    'storageBucket': 'lyraml-dev.appspot.com',
})

# def upload_file(local_file_path, file_name_in_firebase):
#     """Uploads a file to Firebase Storage"""
#     bucket = storage.bucket() # Fetches the default bucket
#     blob = bucket.blob(file_name_in_firebase)
    
#     # New file uploaded
#     blob.upload_from_filename(local_file_path)
    
#     blob.make_public() # TODO: Need to change this later on
#     # Returns the public url
#     return blob.public_url

# # Example usage
# local_file_path = './corgi-test.png'
# file_name_in_firebase = 'corgi-test.png' # You can specify folder structure 
# public_url = upload_file(local_file_path, file_name_in_firebase)
# print(f"Uploaded file accessible at {public_url}")

def upload_data_to_firebase(data, file_name_in_firebase):
    print("type of data: ", type(data))
    bucket = storage.bucket()
    data_size = len(data)
    blob = bucket.blob(file_name_in_firebase)
    blob.upload_from_string(data, content_type='application/octet-stream')
    
    # TODO: Need to change this to some type of signing logic
    blob.make_public()

    return blob.public_url, data_size


def upload_text_to_firebase(text_data, file_name_in_firebase):
    byte_stream = io.BytesIO(text_data.encode('utf-8'))

    bucket = storage.bucket()
    encoded_data = text_data.encode('utf-8')
    byte_stream = io.BytesIO(encoded_data)
    data_size = len(encoded_data)
    blob = bucket.blob(file_name_in_firebase)
    blob.upload_from_file(byte_stream, content_type='text/plain')
    
    # TODO: Need to change this to some type of signing logic
    blob.make_public()

    return blob.public_url, data_size


def download_json_file(url):
    """Download a file from a Firebase URL and save it locally."""
    response = requests.get(url)
    response.raise_for_status()  # This will raise an exception for HTTP errors

    return json.loads(response.content)


def download_file(url):
    """Download a file from a Firebase URL and save it locally."""
    response = requests.get(url)
    response.raise_for_status()  # This will raise an exception for HTTP errors

    return response.content
