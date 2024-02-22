import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from conftest import driver_chrome, our_website



# Тест 01
def test_element_currency(driver):
    """Находим элемент выбора валют и проверяем можно ли нажать"""
    
    driver.maximize_window()
    element_money = "[data-widget='selectedCurrency']"
    find_money = driver.find_element(By.CSS_SELECTOR, element_money)

    find_money.click()

    assert find_money.is_enabled(), 'Элемент не доступен'


# Тест 02
def test_find_element_seller(driver_chrome):
    """Нахождение и выделение элемента "Стать продавцом"  """

    driver_chrome.get("https://ozon.by")

    element_seller = driver_chrome.find_element(By.XPATH, "(//*[@class='d4153-a'])[1]")

    assert element_seller.is_displayed(), 'Элемент отсутствует'


# Тест 03
def test_poisk_string(driver_chrome):
    """нахождение строки поиска и ввод значения в строку поиска"""

    driver_chrome.get('https://ozon.by')
    element = driver_chrome.find_element(By.XPATH, '//input')
    element.click()
    element.send_keys('электроника')
    time.sleep(3)

    assert element.is_enabled(), 'Элемент не доступен'


# Тест 04
def test_poisk_elementa_i_perehod(chrome):
    """Найти эелемент и кликнуть"""

    chrome.get('https://ozon.by')
    element_clothes = chrome.find_element(By.LINK_TEXT, "Одежда и обувь")

    element_clothes.click()

    element_clothes_true = chrome.find_element(By.CSS_SELECTOR, "[class='de9 fd']")

    assert element_clothes_true.is_displayed(), 'Элемент отсутствует'


# Тест 05
def test_poisk_elementa(driver_chrome):
    """поиск элемента корзина"""

    driver_chrome.maximize_window()
    driver_chrome.get('https://ozon.by')
    # element_korzina = "a[href='/cart'"
    element_korzina = driver_chrome.find_element(By.CSS_SELECTOR, "a[href='/cart'")

    assert element_korzina.is_displayed(), "Элемент отсутствует"
