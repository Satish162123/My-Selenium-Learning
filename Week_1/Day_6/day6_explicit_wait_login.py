from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys

# UPDATE THIS PATH
driver_path = r"F:/Satish/chromedriver-win64/chromedriver.exe"

def main():
    driver = webdriver.Chrome(service=Service(driver_path))
    wait = WebDriverWait(driver, 10)

    try:
        print("Opening SauceDemo website")
        driver.get("https://www.saucedemo.com/")

        try:
            username = wait.until(
                EC.visibility_of_element_located((By.ID, "user-name"))
            )
            username.send_keys("standard_user")
        except TimeoutException:
            print("ERROR: Username field not visible")
            driver.quit()
            sys.exit(1)

        try:
            password = wait.until(
                EC.visibility_of_element_located((By.ID, "password"))
            )
            password.send_keys("secret_sauce")
        except TimeoutException:
            print("ERROR: Password field not visible")
            driver.quit()
            sys.exit(1)

        try:
            login_btn = wait.until(
                EC.element_to_be_clickable((By.ID, "login-button"))
            )
            login_btn.click()
        except TimeoutException:
            print("ERROR: Login button not clickable")
            driver.quit()
            sys.exit(1)

        try:
            wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
            )
            print("Login successful — Inventory page loaded")
        except TimeoutException:
            print("ERROR: Inventory page did not load")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
