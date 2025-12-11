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
        driver.get("https://demoqa.com/menu/")
        main_item_2 = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Main Item 1']")))
        actions.move_to_element(main_item_2).perform()
        time.sleep(1)

        sub_list = driver.find_element(By.XPATH, "//a[text()='SUB SUB LIST »']")
        actions.move_to_element(sub_list).perform()
        time.sleep(1)

        sub_item_2 = driver.find_element(By.XPATH, "//a[text()='Sub Sub Item 2']")
        actions.move_to_element(sub_item_2).perform()
        
        print("Hovered over 'Sub Sub Item 2' successfully.", sub_item_2.text)

        ss = "hover_menu_result.png"
        driver.save_screenshot(ss)
        print("Screenshot saved:", os.path.abspath(ss))

    finally:
        time.sleep(1)
        driver.quit()
if __name__ == "__main__":
    main()