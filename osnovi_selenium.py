import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture
def chrome():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.close()
    driver.quit()

#Тест 01
def test_max_window(chrome):
    """открытие  в максимальном разрешении экрана"""

    chrome.get("https://ozon.by")
    time.sleep(2)


#Тест 02
def test_min_window(chrome):
    """открытие  в минимальном разрешении экрана"""

    chrome.minimize_window()
    chrome.get("https://ozon.by")
    time.sleep(2)

#Тест 03
def test_poisk_string(chrome):
    """нахождение строки поиска и ввод значения в строку поиска"""

    chrome.get('https://ozon.by')
    element = chrome.find_element(By.XPATH, '//input')
    element.send_keys('elektronika')
    time.sleep(3)

#Тест 04
def test_double_window(chrome):
    """Переход в первую ссылку, после во вторую и обратно"""

    chrome.get('https://ozon.by')
    time.sleep(2)
    chrome.get("https://habr.com/ru/feed/")
    time.sleep(1)
    chrome.back()

#Тест 05
def test_poisk_elementa(chrome):
    """поиск элемента корзина"""

    chrome.maximize_window()
    chrome.get('https://ozon.by')
    #element_korzina = "a[href='/cart'"
    element_korzina = chrome.find_element(By.CSS_SELECTOR, "a[href='/cart'")

    if element_korzina.is_displayed():
        print('Element naiden')
    else:
        print('Element ne naiden')
