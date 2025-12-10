# day2_saucedemo_login.py
# Purpose: Demo of locating elements by ID and performing login on saucedemo
# Usage: python day2_saucedemo_login.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, sys

# === EDIT: set this to your chromedriver if not on PATH ===
driver_path = r"F:/Satish/chromedriver-win64/chromedriver.exe"   # Windows example
# driver_path = "/Users/you/drivers/chromedriver"  # macOS/Linux example

def create_driver():
    if driver_path and not os.path.exists(driver_path):
        print("ERROR: chromedriver not found at:", driver_path)
        sys.exit(1)
    service = Service(driver_path) if driver_path else None
    return webdriver.Chrome(service=service) if service else webdriver.Chrome()

def main():
    driver = create_driver()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get("https://www.saucedemo.com/")
        # wait for username field to be present
        user = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        pwd = driver.find_element(By.ID, "password")
        login = driver.find_element(By.ID, "login-button")

        # perform login
        user.clear()
        user.send_keys("standard_user")
        pwd.clear()
        pwd.send_keys("secret_sauce")
        login.click()

        # wait for inventory page to load (sample element)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        print("Login successful — Page Title:", driver.title)

        # take a screenshot for evidence
        screenshot_path = os.path.join(os.getcwd(), "saucedemo_after_login.png")
        driver.save_screenshot(screenshot_path)
        print("Saved screenshot:", screenshot_path)

    except Exception as e:
        print("ERROR during saucedemo login:", repr(e))
        # optional: save screenshot on failure
        try:
            fn = os.path.join(os.getcwd(), "saucedemo_error.png")
            driver.save_screenshot(fn)
            print("Saved error screenshot:", fn)
        except Exception:
            pass
    finally:
        time.sleep(1)
        driver.quit()

if __name__ == "__main__":
    main()
