import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService, Service

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By


@pytest.fixture
def chrome():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


#def test_by_name(chrome):
    #chrome.get('https://ozon.by/')
   # name = 'yandex-tableau-widget'

    #assert chrome.find_element(By.NAME, name)

def test_lenta(chrome):
    chrome.get('https://habr.com/ru/articles/667238/')
    text = 'Научпоп'
    assert chrome.find_element(By.LINK_TEXT, text)

def test_by_class_name(chrome):
        chrome.get('https://habr.com/ru/articles/667238/')
        class_name = 'tm-adfox-banner__container'
        elements = chrome.find_elements(By.CLASS_NAME, class_name)
        assert len(elements) == 4
