from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_inventory_displayed(self):
        return self.wait.until(
            EC.presence_of_element_located(self.INVENTORY_ITEM)
        ).is_displayed()
