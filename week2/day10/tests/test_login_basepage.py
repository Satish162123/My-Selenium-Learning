import pytest 
from pages.login_page import LoginPage 
from pages.inventory_page import InventoryPage 
 
@pytest.mark.smoke 
def test_valid_login_basepage(driver): 
    login_page = LoginPage(driver) 
    inventory_page = InventoryPage(driver) 
 
    login_page.load() 
    login_page.login("standard_user", "secret_sauce") 
    assert inventory_page.is_inventory_displayed()

@pytest.mark.regression 
def test_invalid_login_basepage(driver): 
    login_page = LoginPage(driver) 
    login_page.load() 
    login_page.login("invalid_user", "invalid_password") 
    assert "Username and password do not match" in login_page.get_error_message()