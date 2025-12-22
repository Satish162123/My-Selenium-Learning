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

@pytest.mark.parametrize(
    "username,password",
    [
        ("wrong_user", "secret_sauce"),
        ("standard_user", "wrong_pass"),
        ("", ""),
    ]
)
def test_invalid_login_multiple_data(driver, username, password):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")

    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))
    assert error.is_displayed()
