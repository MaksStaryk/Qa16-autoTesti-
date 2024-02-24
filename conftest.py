import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(autouse=False)
def driver_chrome():
    print('Start driver GoogleChrome\n')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.close()
    driver.quit()

    print('Finish')


@pytest.fixture()
def driver_firefox():
    print("Start driver FireFox\n")
    driver1 = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver1.implicitly_wait(8)
    yield driver1
    driver1.close()
    driver1.quit()
    print("Finish test")


# @pytest.fixture(autouse=True)
# def pop_up_window(driver_chrome):
#     element = driver_chrome.find_element(By.CSS_SELECTOR, "[class='a2437-a4']")
#     element.click()


@pytest.fixture(autouse=False)
def our_website(driver_chrome):
    driver_chrome.get("https://ozon.by")


@pytest.fixture
def web_page_phone(driver_chrome):
    driver_chrome.get("https://ozon.by/category/smartfony-15502/")



