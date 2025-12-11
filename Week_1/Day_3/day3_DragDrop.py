from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, sys

# Set up the Chrome WebDriver
driver_path = r"F:/Satish/chromedriver-win64/chromedriver.exe"

def create_driver():
    if not os.path.exists(driver_path):
        print("Chrome Driver not found. Please check the path.")
        sys.exit(1)
    return webdriver.Chrome(service=Service(driver_path))

def main():
    driver = create_driver()
    wait = WebDriverWait(driver, 6)
    actions = ActionChains(driver)

    try:
        driver.get("https://demoqa.com/droppable/")
        source = wait.until(EC.presence_of_element_located((By.ID, "draggable")))
        target = driver.find_element(By.ID, "droppable")

        actions.drag_and_drop(source, target).perform()
        time.sleep(1)

        result_text = target.text 
        print("Drop Area Text After:", result_text) 
 
        ss = "drag_drop_result.png" 
        driver.save_screenshot(ss) 
        print("Screenshot saved:", os.path.abspath(ss)) 
 
    finally: 
        driver.quit() 
 
if __name__ == "__main__": 
    main()