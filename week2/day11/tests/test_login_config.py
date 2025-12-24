import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config_reader import ConfigReader

@pytest.mark.smoke
def test_valid_login_config(driver):
    login_page = LoginPage(driver) 
    inventory_page = InventoryPage(driver) 
 
    username = ConfigReader.get("credentials", "valid_username") 
    password = ConfigReader.get("credentials", "valid_password") 
 
    login_page.load() 
    login_page.login(username, password) 
 
    assert inventory_page.is_inventory_displayed() 
 
 
@pytest.mark.regression 
def test_invalid_login_config(driver): 
    login_page = LoginPage(driver) 
 
    username = ConfigReader.get("credentials", "invalid_username") 
    password = ConfigReader.get("credentials", "invalid_password") 
 
    login_page.load() 
    login_page.login(username, password) 
 
    assert "Username and password do not match" in login_page.get_error_message()