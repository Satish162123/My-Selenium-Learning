from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config_reader import ConfigReader

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name") 
    PASSWORD = (By.ID, "password") 
    LOGIN_BTN = (By.ID, "login-button") 
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']") 
 
    def load(self): 
        url = ConfigReader.get("app", "base_url") 
        self.open(url) 
        self.wait_for_visibility(self.USERNAME) 
 
    def login(self, username, password): 
        self.type(self.USERNAME, username) 
        self.type(self.PASSWORD, password) 
        self.click(self.LOGIN_BTN) 
 
    def get_error_message(self): 
        return self.get_text(self.ERROR_MSG)