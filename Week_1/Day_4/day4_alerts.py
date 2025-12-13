from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, sys

driver_path = r"F:/Satish/chromedriver-win64/chromedriver.exe"

def main():
    driver = webdriver.Chrome(service=Service(driver_path))
    wait = WebDriverWait(driver, 6)

    try:
        driver.get("https://demoqa.com/alerts")
        driver.maximize_window()

        #simple alert
        driver.find_element(By.ID, "alertButton").click()
        alert = driver.switch_to.alert
        print("Alert Text:", alert.text)
        alert.accept()
        time.sleep(1)

        #confirm alert
        driver.find_element(By.ID, "confirmButton").click()
        alert = driver.switch_to.alert
        print("Confirm Alert Text:", alert.text)
        alert.dismiss()
        time.sleep(1)

        #prompt alert
        driver.find_element(By.ID, "promtButton").click()
        alert = driver.switch_to.alert
        alert.send_keys("Satish Kadari")
        alert.accept()
        time.sleep(1)

        #Print confirmation message
        result  = driver.find_element(By.ID, "promptResult").text
        print("Prompt Result Text:", result)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()