from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, sys

driver_path = r"F:/Satish/chromedriver-win64/chromedriver.exe"

def main():
    driver = webdriver.Chrome(service=Service(driver_path))
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://demoqa.com/browser-windows")
        driver.maximize_window()

        #open new tab
        driver.find_element(By.ID, "tabButton").click()
        handles = driver.window_handles

        #switch to new tab
        driver.switch_to.window(handles[-1])
        heading = driver.find_element(By.ID, "sampleHeading").text
        print("New Tab Heading:", heading)

        # Close new tab
        driver.close()

        #switch back to main window
        driver.switch_to.window(handles[0])

        #open new window message
        driver.find_element(By.ID, "messageWindowButton").click()
        handles = driver.window_handles

        #Switch to new window
        driver.switch_to.window(handles[-1])
        print("Message window Text:", driver.find_element(By.TAG_NAME, "body").text)

        # Close new window
        driver.close()
        driver.switch_to.window(handles[0])

    finally:
        driver.quit()
        
if __name__ == "__main__":
    main()