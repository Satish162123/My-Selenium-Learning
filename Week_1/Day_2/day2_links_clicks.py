# day2_links_clicks.py
# Purpose: Demonstrate link_text and partial_link_text locating on demoqa links page
# Usage: python day2_links_clicks.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, sys

driver_path = r"F:/Satish/chromedriver-win64/chromedriver.exe"  # update

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
        driver.get("https://demoqa.com/links")

        # link_text example: "Home"
        # Note: On this page "Home" link opens a new tab. We'll click and then switch.
        home_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Home")))
        home_link.click()

        # switch to new window
        handles = driver.window_handles
        if len(handles) > 1:
            driver.switch_to.window(handles[-1])
            print("Switched to new tab — Title:", driver.title)
            # close new tab and switch back
            driver.close()
            driver.switch_to.window(handles[0])
        else:
            print("Home link did not open a new tab (unexpected).")

        # partial link text: click the link that contains "created"
        created_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Created")))
        created_link.click()

        # check element that shows API response — wait for visible result text
        result = wait.until(EC.visibility_of_element_located((By.ID, "linkResponse")))
        print("Clicked 'Created' link — response:", result.text)

        ss = os.path.join(os.getcwd(), "demoqa_links_result.png")
        driver.save_screenshot(ss)
        print("Saved screenshot:", ss)

    except Exception as e:
        print("ERROR during links test:", repr(e))
        try:
            fn = os.path.join(os.getcwd(), "links_error.png")
            driver.save_screenshot(fn)
            print("Saved error screenshot:", fn)
        except Exception:
            pass
    finally:
        time.sleep(1)
        driver.quit()

if __name__ == "__main__":
    main()
