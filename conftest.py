import pytest
import os
import sys
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DAY12_DIR = os.path.join(ROOT_DIR, "week2", "day12")

if DAY12_DIR not in sys.path:
    sys.path.insert(0, DAY12_DIR)

driver_path = r"F:/Satish/chromedriver-win64/chromedriver.exe"  # UPDATE
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()
    
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            root_dir = os.path.dirname(__file__)
            screenshots_dir = os.path.join(root_dir, "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)

