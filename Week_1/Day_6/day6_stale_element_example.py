from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import sys

# UPDATE THIS PATH
driver_path = r"F:/Satish/chromedriver-win64/chromedriver.exe"

def main():
    driver = webdriver.Chrome(service=Service(driver_path))
    wait = WebDriverWait(driver, 10)

    try:
        print("Opening SauceDemo website")
        driver.get("https://www.saucedemo.com/")

        username = wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username.send_keys("standard_user")

        print("Refreshing page to simulate DOM change")
        driver.refresh()

        try:
            # ❌ OLD reference — expected to fail
            username.send_keys("will fail")
        except StaleElementReferenceException:
            print("StaleElementReferenceException caught — re-locating element")

            # ✅ Re-locate element
            username = wait.until(
                EC.presence_of_element_located((By.ID, "user-name"))
            )
            username.clear()
            username.send_keys("standard_user")

            print("Stale element handled successfully")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
