from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.locators_for_phone_page import *


class PhonePage(BasePage):

    def open_phone_page(self):
        """Open Phone page"""

        self.driver_chrome.get("https://ozon.by/category/smartfony-15502/")










