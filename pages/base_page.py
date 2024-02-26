import time

from selenium.webdriver.support.ui import Select


class BasePage:

    def __init__(self, driver):
        self.driver_chrome = driver

    def title(self):
        return self.driver_chrome.title

    def find_element(self, args):
        return self.driver_chrome.find_element(*args)

    def find_elements(self, args):
        return self.driver_chrome.find_elements(*args)

    def scroll_to_basement(self, locator):
        self.driver_chrome.execute_script("arguments[0].scrollIntoView();", self.find_element(locator))

    def get_attribute(self, locator, call: str):
        element = self.find_element(locator)
        return element.get_attribute(call)

    def get_text(self, xpath):
        text_cat = self.find_element(xpath)
        return text_cat.text

    def submit(self, xpath):
        element = self.find_element(xpath)
        return element.submit()

    def clear_text(self, text: str, locator):
        some_string = self.find_element(locator)
        some_string.click()
        some_string.send_keys(text)
        time.sleep(2)
        some_string.clear()

    def select_some(self, locator, text: str):
        select_element = Select(self.find_element(locator))
        select_element.select_by_visible_text(text)

    def switch_to_page(self, locator_1):
        self.driver_chrome.current_window_handle
        self.scroll_to_basement(locator_1)
        self.find_element(locator_1).click()
        tabs = self.driver_chrome.window_handles
        self.driver_chrome.switch_to.window(tabs[1])

        return self.driver_chrome.current_url
