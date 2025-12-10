# day2_demoqa_textbox.py
# Purpose: Fill the DemoQA "Text Box" form and submit.
# Usage: python day2_demoqa_textbox.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, sys

driver_path = r"F:/Satish/chromedriver-win64/chromedriver.exe" # update accordingly

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
        driver.get("https://demoqa.com/text-box")

        # Wait for the Full Name input to be present (id=userName)
        full_name = wait.until(EC.presence_of_element_located((By.ID, "userName")))
        email = driver.find_element(By.ID, "userEmail")
        current_address = driver.find_element(By.ID, "currentAddress")
        permanent_address = driver.find_element(By.ID, "permanentAddress")

        # Fill form
        full_name.send_keys("Satish K")
        email.send_keys("satish@example.com")
        current_address.send_keys("123 Test Street, Bangalore")
        permanent_address.send_keys("456 Home Lane, Hyderabad")

        # Submit button (id=submit) may be hidden behind footer; use JS click if necessary
        submit_btn = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].click();", submit_btn)

        # Wait for output area to appear
        output = wait.until(EC.visibility_of_element_located((By.ID, "output")))
        print("Form submitted — output text snippet:", output.text[:120])

        # screenshot
        ss = os.path.join(os.getcwd(), "demoqa_textbox_after_submit.png")
        driver.save_screenshot(ss)
        print("Saved screenshot:", ss)

    except Exception as e:
        print("ERROR during demoqa textbox:", repr(e))
        try:
            fn = os.path.join(os.getcwd(), "demoqa_error.png")
            driver.save_screenshot(fn)
            print("Saved error screenshot:", fn)
        except Exception:
            pass
    finally:
        time.sleep(1)
        driver.quit()

if __name__ == "__main__":
    main()
