from locators.locators_for_main_page import search_string



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


