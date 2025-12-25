from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_list")

    def is_inventory_displayed(self):
        return self.is_visible(self.INVENTORY_ITEM)
    