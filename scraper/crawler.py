from abc import ABC
import json


class Crawler(ABC):
    def __init__(self, url):
        self.data = {}
        self.url = url

    def export_json(self) -> None:
        try:
            with open(f"output_files/{type(self).__name__}.json", "r+", encoding='utf-8') as f:
                f.write(json.dumps(self.data, indent=4, ensure_ascii=False))
        except FileNotFoundError:
            print("no such file created yet, creating now !")
            with open(f"output_files/{type(self).__name__}.json", "w", encoding='utf-8') as f:
                f.write(json.dumps(self.data, indent=4, ensure_ascii=False))

    def import_json(self) -> None:
        try:
            json_data = json.load(open(f"output_files/{type(self).__name__}.json", "r", encoding='utf-8'))
            for item in json_data:
                print(json_data[item])
        except FileNotFoundError:
            print("No such json file found in system")