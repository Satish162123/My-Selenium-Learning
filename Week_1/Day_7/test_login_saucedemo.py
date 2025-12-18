import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, sys, os

driver_path = r"F:/Satish/chromedriver-win64/chromedriver.exe"   # UPDATE THIS

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service = Service(driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    user_name = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    user_name.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    inventory_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    assert inventory_container.is_displayed(), "Login failed - Inventory container not displayed"


def test_invalid_login(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    user_name = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    user_name.send_keys("invalid_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("invalid_password")

    driver.find_element(By.ID, "login-button").click()

    inventory_container_1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))

    assert "uername and password do not match" in inventory_container_1.text, "Error message not displayed for invalid login"