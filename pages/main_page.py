
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.locators_for_main_page import *


class MainPage(BasePage, LocatorsMain):

    def open(self):
        self.driver_chrome.get("https://ozon.by")

    def search_string(self, some_text):
        analog_google = self.find_element(self.SEARCH_STRING)
        analog_google.click()
        analog_google.send_keys(some_text)
        analog_google.send_keys(Keys.ENTER)

    def enter_world(self, text):
        self.open()
        search_input = self.find_element(self.SEARCH_STRING)
        search_input.click()
        search_input.send_keys(text)
        search_input.send_keys(Keys.ENTER)

    def enter_number(self, num: int):
        search_input = self.find_element(self.SEARCH_STRING)
        search_input.click()
        search_input.send_keys(num)
        search_input.send_keys(Keys.ENTER)

    def location(self):
        street_element = self.find_element(self.DELIVERY_ADDRESS).click()
        on_map = self.find_element(self.SELECT_ON_THE_MAP).click()


    def access(self):
        access_element = self.find_element(self.ACESS).click()

    def food(self):

        self.find_element(self.THINGS).click()

    def search_field(self, some_text):
        analog_google = self.find_element(self.SEARCH_STRING)
        analog_google.click()
        analog_google.send_keys(some_text)













