import requests
from bs4 import BeautifulSoup
from scraper.crawler import Crawler
import utils.constants as const


class MobileEye(Crawler):
    def __init__(self):
        super().__init__(const.beach_bum)

    def query(self):
        response = requests.get(const.mobile_eye)
        if response.status_code == 200:
            try:
                html_content = response.text  # Get the HTML content
                soup = BeautifulSoup(html_content, 'html.parser')
                job_name = soup.find_all('h3')
                for job in job_name:
                    name = job.text
                    location = job.find_next().get_text().strip()
                    url = "https://careers.mobileye.com" + job.find_previous('a').get('href')
                    if 'Israel' not in location:
                        continue
                    if "FILTER" in name:
                        continue
                    else:
                        self.data[url] = {}
                        self.data[url]['title'] = name
                        self.data[url]['location'] = location

            except (ValueError, KeyError) as e:
                print(f"Error parsing the response: {e}")

        else:
            print(f"Failed to retrieve data: {response.status_code}")

    def extract_data_from_job(self):
        self.query()
        for url in self.data.keys():
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    html_content = response.text  # Get the HTML content
                    soup = BeautifulSoup(html_content, 'html.parser')
                    information = soup.find('div',
                                            class_='list_box')
                    requirements = information.find_next('div')
                    responsibility = information.get_text().strip()
                    requirements = requirements.get_text().strip()
                    self.data[url]['responsibility'] = responsibility
                    self.data[url]['requirements'] = requirements

                except (ValueError, KeyError) as e:
                    print(f"Error parsing the response: {e}")

                except IndexError:
                    print("Index out of bounds")
                    print(url)
            else:
                print("status code wasn't 200 - failed to perfectly connect with the server")

    def print_jobs(self):
        for keys in self.data.keys():
            for key in self.data[keys]:
                if 'title' in key:
                    print(f"{key}: {self.data[keys][key]}")
                else:
                    print(f"{self.data[keys][key]}")
            print(f"url : {keys}")
            print("*" * 50)
