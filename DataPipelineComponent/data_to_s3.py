from utils import *
import os
from s3_sync import S3Sync
from dotenv import load_dotenv
load_dotenv()

class DataDumpS3:
    def __init__(self, file_path):
        self.bucket_name = os.getenv("AWS_S3_BUCKET")
        self.file_path= file_path
    
    def dump_data(self):
        for file in os.listdir(self.file_path):
            if file.endswith(".xml"):
                data_dir=os.path.join(os.getcwd(),self.file_path)
                print(data_dir) #c:\Users\chira\OneDrive\Documents\stack-overflow-python-query-prediction\DataPipelineComponent\main_data 
                s3_uri=f"s3://{self.bucket_name}/stack_overflow_data" #s3://pythonquerystackoverflow/stack_overflow_data
                S3Sync.s3_json_folder_sync(data_dir,s3_uri)
            else:
                return "Data failed to store in s3 bucket"

if __name__=="__main__":
    print(DataDumpS3("main_data").dump_data())

    