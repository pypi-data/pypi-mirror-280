import pandas as pd
from datasets import Dataset, DatasetDict
from huggingface_hub import HfApi, create_repo

class DataFrameUploader:
    def __init__(self, df: pd.DataFrame, hf_token: str, repo_name: str, username: str):
        self.df = df
        self.hf_token = hf_token
        self.repo_name = repo_name
        self.username = username
        self.dataset_dict = None
        
    def verify_dataframe(self):
        if 'questions' not in self.df.columns or 'answers' not in self.df.columns:
            raise ValueError("The dataframe must have columns named 'questions' and 'answers'.")
        print("Dataframe verified: columns 'questions' and 'answers' are present.")
        return True
    
    def process_data(self):
        if self.verify_dataframe():
            raw_content_questions = list(self.df['questions'])
            raw_content_answers = list(self.df['answers'])
            train_data = {
                'questions': raw_content_questions,
                'answers': raw_content_answers
            }
            train_dataset = Dataset.from_dict(train_data)
            self.dataset_dict = DatasetDict({'train': train_dataset})
            print("Data processed into DatasetDict.")
        
    def push_to_hub(self):
        if self.dataset_dict:
            api = HfApi()
            create_repo(self.repo_name, token=self.hf_token, private=False)  # Set private=True if you want it to be a private dataset
            app_id = f"{self.username}/{self.repo_name}"
            print(f"Repository created: {app_id}")
            self.dataset_dict.push_to_hub(app_id, token=self.hf_token)
            print("Dataset pushed to Hugging Face Hub.")
        else:
            raise ValueError("DatasetDict is not created. Ensure process_data() is called after dataframe verification.")
