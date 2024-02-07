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
def test_element_currency(chrome):
    """Находим элемент выбора валют и проверяем можно ли нажать"""


    chrome.maximize_window()
    chrome.get("https://ozon.by")

    element_money = chrome.find_element(By.CSS_SELECTOR, "[class='od7 ga26-a undefined'] ")

    time.sleep(3)

    element_money.click()

    time.sleep(4)

    assert element_money.is_enabled(), 'Элемент не доступен'


#Тест 02
def test_find_element_seller(chrome):
    """Нахождение и выделение элемента "Стать продавцом"  """


    chrome.get("https://ozon.by")

    element_seller = chrome.find_element(By.LINK_TEXT, "Стать продавцом")
    time.sleep(2)

    assert element_seller.is_displayed(), 'Элемент отсутствует'



#Тест 03
def test_poisk_string(chrome):
    """нахождение строки поиска и ввод значения в строку поиска"""

    chrome.get('https://ozon.by')
    element = chrome.find_element(By.XPATH, '//input')
    element.click()
    element.send_keys('электроника')
    time.sleep(3)

    assert element.is_enabled(), 'Элемент не доступен'

#Тест 04
def test_poisk_elementa_i_perehod(chrome):
    """Найти эелемент и кликнуть"""


    chrome.get('https://ozon.by')
    element_clothes = chrome.find_element(By.LINK_TEXT, "Одежда и обувь")

    element_clothes.click()

    element_clothes_true = chrome.find_element(By.CSS_SELECTOR, "[class='de9 fd']")

    assert element_clothes_true.is_displayed(), 'Элемент отсутствует'



#Тест 05
def test_poisk_elementa(chrome):
    """поиск элемента корзина"""


    chrome.maximize_window()
    chrome.get('https://ozon.by')
    #element_korzina = "a[href='/cart'"
    element_korzina = chrome.find_element(By.CSS_SELECTOR, "a[href='/cart'")

    assert element_korzina.is_displayed(), "Элемент отсутствует"

