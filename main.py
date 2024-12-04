import time
from scraper.beach_bum import BeachBum
from scraper.mobile_eye import MobileEye
from scraper.moon_active import MoonActive


def main():
    start_time = time.time()
    # beach_bum job data
    beach_bum = BeachBum()
    beach_bum.extract_data_from_job()
    beach_bum.upload_to_s3()
    # mobile_eye job data
    mobile_eye = MobileEye()
    mobile_eye.extract_data_from_job()
    mobile_eye.upload_to_s3()
    # moon_active job data
    moon = MoonActive()
    moon.extract_data_from_job()
    moon.upload_to_s3()
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)
    print(f"The time it took to run: {elapsed_time} seconds")
