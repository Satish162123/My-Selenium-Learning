# first_script.py
# Simple Selenium starter script: open 3 websites and print titles.
# Works with Selenium 4 and ChromeDriver.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import sys
import os

def main():
    # === EDIT THIS: put the full path to your chromedriver executable ===
    # Windows example: r"C:\Users\Satish\drivers\chromedriver.exe"
    # mac/linux example: "/Users/satish/drivers/chromedriver" or "/home/satish/drivers/chromedriver"
    driver_path = r"F:/Satish/chromedriver-win64/chromedriver.exe"

    if not os.path.exists(driver_path):
        print("ERROR: chromedriver not found at:", driver_path)
        print("Make sure you updated driver_path variable in the script.")
        sys.exit(1)

    service = Service(driver_path)

    # Create Chrome driver instance
    driver = webdriver.Chrome(service=service)

    try:
        websites = [
            "https://www.google.com",
            "https://www.youtube.com",
            "https://www.bing.com"
        ]

        for site in websites:
            driver.get(site)
            # small wait so title has time to load
            time.sleep(1)
            print("Opened:", site, "| Title:", driver.title)

    finally:
        # always quit the browser
        driver.quit()

if __name__ == "__main__":
    main()
