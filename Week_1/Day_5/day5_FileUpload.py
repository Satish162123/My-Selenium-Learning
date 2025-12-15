from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, sys

driver_path = r"F:/Satish/chromedriver-win64/chromedriver.exe"   # UPDATE THIS

def main():
    driver = webdriver.Chrome(service=Service(driver_path))
    wait = WebDriverWait(driver,10)

    try:
        driver.get("https://the-internet.herokuapp.com/upload")

        # Path for the input file to be uploaded
        file_path_1 = r"F:/Satish/selenium-learning/Week_1/Day_5/file_upload.txt"

        file_input_1 = wait.until(EC.presence_of_element_located((By.ID, "file-upload")))
        file_input_1.send_keys(file_path_1)

        time.sleep(1)

        driver.find_element(By.ID, "file-submit").click()

        Uploaded_file = wait.until(EC.presence_of_element_located((By.ID, "uploaded-files")))
        print("Uploaded File Name:", Uploaded_file.text)

        print("File upload test PASSED")

    finally:
        time.sleep(1)
        driver.quit()
if __name__ == "__main__":
    main()