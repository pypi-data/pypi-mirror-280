class Judge:
    def __init__(self, name, description, scoring_rubric, passing_criteria, dataset_tag):
        self.name = name
        self.description = description
        self.scoring_rubric = scoring_rubric
        self.passing_criteria = passing_criteria
        self.dataset_tag = dataset_tag

    def to_json(self):
        return {
            'name': self.name,
            'dataset_tag': self.dataset_tag,
            'description': self.description,
        }