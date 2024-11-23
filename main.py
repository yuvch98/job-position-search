import time
from scraper.beach_bum import BeachBum
from scraper.mobile_eye import MobileEye
from scraper.moon_active import MoonActive

if __name__ == '__main__':
    start_time = time.time()
    beach_bum = BeachBum()
    beach_bum.extract_data_from_job()
    beach_bum.print_jobs()
    print("*"*100)
    mobile_eye = MobileEye()
    mobile_eye.extract_data_from_job()
    mobile_eye.print_jobs()
    print("*"*100)
    moon = MoonActive()
    moon.extract_data_from_job()
    moon.print_jobs()
    end_time = time.time()
    final_time = end_time - start_time
    print(f"time it took was {round(final_time, 2)} seconds")
