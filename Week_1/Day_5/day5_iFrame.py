from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = r"F:/Satish/chromedriver-win64/chromedriver.exe"   # UPDATE THIS

def main():
    driver = webdriver.Chrome(service=Service(driver_path))
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(
            "https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe_height_width"
        )

        # Switch to outer iframe
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframeResult")))

        # Switch to inner iframe
        inner_iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        driver.switch_to.frame(inner_iframe)

        # Read guaranteed element
        heading = driver.find_element(By.TAG_NAME, "h1").text
        print("Iframe Heading:", heading)

        # OPTIONAL: check if <p> exists before reading
        paragraphs = driver.find_elements(By.TAG_NAME, "p")
        if paragraphs:
            print("Iframe Paragraph:", paragraphs[0].text)
        else:
            print("No <p> tag present inside iframe (expected behavior)")

        # Switch back to main page
        driver.switch_to.default_content()
        print("Iframe handling PASSED")

    finally:
        time.sleep(1)
        driver.quit()

if __name__ == "__main__":
    main()
