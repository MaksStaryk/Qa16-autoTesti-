from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.phone_locators import PhonePageLocator


class PhonePage(BasePage, PhonePageLocator):

    def open_phone_page(self):
        """Open Phone page"""

        self.driver_chrome.get("https://ozon.by/category/smartfony-15502/")

    def click_add_basket(self, locator):
        """Кликаем по элементу"""

        self.find_element(locator).click()

    def click_clear_basket(self):
        """Кликаем по элементу"""
        self.find_element(self.CLEAR_BASKET)

    def click_original_phone(self):
        self.find_element(self.BUTTON_ORIGINAL_PHONE).click()

    def click_three_days(self):
        """Кликаем по элементу"""

        self.find_element(self.THREE_DAYS_BUTTON).click()

    def send_click(self, locator):
        self.find_element(locator).send_keys(Keys.ENTER)
