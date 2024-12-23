from abc import ABC
import json
import boto3
from utils.constants import bucket_name


class Crawler(ABC):
    def __init__(self, url):
        self.data = {}
        self.url = url

    def upload_to_s3(self):
        json_data = self.export_json()
        s3 = boto3.client('s3')
        try:
            object_name = f"{type(self).__name__}.json"  # File name in the bucket
            s3.put_object(
                Bucket=bucket_name,
                Key=object_name,
                Body=json_data,
                ContentType="application/json"
            )
            print(f"JSON data successfully uploaded to {bucket_name}/{object_name}")
        except Exception as e:
            print(f"Error uploading to S3: {e}")

    def export_json(self) -> str:
        json_data = json.dumps(self.data, indent=4, ensure_ascii=False)
        return json_data

    def import_json(self) -> None:
        try:
            json_data = json.load(open(f"output_files/{type(self).__name__}.json", "r", encoding='utf-8'))
            for item in json_data:
                print(json_data[item])
        except FileNotFoundError:
            print("No such json file found in system")
