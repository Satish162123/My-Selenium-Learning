import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = r"F:/Satish/chromedriver-win64/chromedriver.exe"  # UPDATE
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()
    