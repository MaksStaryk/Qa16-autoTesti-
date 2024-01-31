import time
from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
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
    """открытие  в  разрешении экрана width = 1920 height = 1080"""

    expect_width = 1920
    expect_height = 1080
    chrome.set_window_size(expect_width,expect_height)

    window_size = chrome.get_window_size()
    chrome.get("https://ozon.by")
    time.sleep(2)

    assert window_size['width'] == expect_width
    assert window_size['height'] == expect_height


#Тест 02
def test_find_element_seller(chrome):
    """Нахождение и выделение элемента "Стать продавцом"  """


    chrome.get("https://ozon.by")

    element_seller = chrome.find_element(By.LINK_TEXT, "Стать продавцом")
    time.sleep(2)
    chrome.execute_script("arguments[0].style.border='2px solid red'", element_seller)
    assert element_seller.is_displayed(), 'Element ne naiden'



#Тест 03
def test_poisk_string(chrome):
    """нахождение строки поиска и ввод значения в строку поиска"""

    chrome.get('https://ozon.by')
    element = chrome.find_element(By.XPATH, '//input')
    element.click()
    element.send_keys('elektronika')
    time.sleep(3)

    assert element.is_enabled(), 'Element ne naiden'

#Тест 04
def test_poisk_elementa_i_perehod(chrome):
    """Найти эелемент и кликнуть"""


    chrome.get('https://ozon.by')
    element_clothes = chrome.find_element(By.LINK_TEXT, "Одежда и обувь")

    element_clothes.click()

    element_clothes_true = chrome.find_element(By.CSS_SELECTOR, "[class='de9 fd']")

    assert element_clothes_true.is_displayed(), 'Element ne naiden'



#Тест 05
def test_poisk_elementa(chrome):
    """поиск элемента корзина"""


    chrome.maximize_window()
    chrome.get('https://ozon.by')
    #element_korzina = "a[href='/cart'"
    element_korzina = chrome.find_element(By.CSS_SELECTOR, "a[href='/cart'")

    assert element_korzina.is_displayed(), "Element ne naiden"

