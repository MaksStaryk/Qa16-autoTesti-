from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.locators_for_phone_page import *


class PhonePage(BasePage):

    def open_phone_page(self):
        """Open Phone page"""

        self.driver_chrome.get("https://ozon.by/category/smartfony-15502/")

    def click_three_days(self):
        """Кликаем по элементу"""

        self.find_element(three_days).click()

    def click_add_basket(self):
        """Кликаем по элементу"""

        self.find_element(add_basket_fir_element).click()

    def click_clear_basket(self):
        """Кликаем по элементу"""
        self.find_element(clear_basket)

    def click_original_phone(self):
        self.find_element(button_original_phone).click()






