import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = r"F:/Satish/chromedriver-win64/chromedriver.exe"  # UPDATE

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(driver_path))
    yield driver
    driver.quit()

@pytest.mark.smoke
def test_valid_login(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")

    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

@pytest.mark.regression
def test_invalid_login(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")

    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("wrong")
    driver.find_element(By.ID, "login-button").click()

    error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))
    assert "Username and password do not match" in error.text
