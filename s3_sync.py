import os

class S3Sync:
    @staticmethod
    def s3_json_folder_sync(folder,aws_bucket_uri): 
        #aws s3 sync <source> <target> [--options]  : The s3 sync command synchronizes the contents of a bucket and a directory
        command=f"aws s3 sync {folder} {aws_bucket_uri}"
        os.system(command)

    @staticmethod
    def sync_folder_from_s3(folder,aws_bucket_uri):
        command=f"aws s3 sync {aws_bucket_uri} {folder}"
        os.system(command)

#os.system("echo 'hello'")