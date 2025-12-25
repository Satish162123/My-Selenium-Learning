from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = get_logger(self.__class__.__name__)

    def open(self, url):
        self.logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def wait_for_visibility(self, locator):
        self.logger.debug(f"Waiting for visibility of element: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")
        self.wait_for_visibility(locator).click()

    def type(self, locator, text):
        self.logger.info(f"Typing into element: {locator}")
        element = self.wait_for_visibility(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        self.logger.info(f"Getting text from element: {locator}")
        return self.wait_for_visibility(locator).text

    def is_visible(self, locator):
        try:
            self.wait_for_visibility(locator)
            return True
        except Exception:
            return False
