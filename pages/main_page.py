
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.locators_for_main_page import *


class MainPage(BasePage):

    def open(self):
        self.driver_chrome.get("https://ozon.by")

    def search_string(self, some_text):
        analog_google = self.find_element(search_string)
        analog_google.click()
        analog_google.send_keys(some_text)
        analog_google.send_keys(Keys.ENTER)

    def enter_world(self, text):
        self.open()
        search_input = self.find_element(search_string)
        search_input.click()
        search_input.send_keys(text)
        search_input.send_keys(Keys.ENTER)

    def enter_number(self, num: int):
        search_input = self.find_element(search_string)
        search_input.click()
        search_input.send_keys(num)
        search_input.send_keys(Keys.ENTER)

    def location(self):
        street_element = self.find_element(delivery_address).click()
        on_map = self.find_element(select_on_the_map).click()


    def access(self):
        access_element = self.find_element(acess).click()

    def food(self):

        self.find_element(things).click()

    def search_field(self, some_text):
        analog_google = self.find_element(search_string)
        analog_google.click()
        analog_google.send_keys(some_text)












