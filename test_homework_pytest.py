import time
import pytest

from selenium.webdriver import Keys
from conftest import chrome
from selenium.webdriver.common.by import By
from conftest import our_website
from conftest import web_page_phone

list_other_think = ["книга", "сковородка", "стиральная машина", "ноутбук"]


@pytest.mark.parametrize("other_things", list_other_think)
def test_string_search(chrome, other_things, our_website):
    """В строке поиска вводим названия предметов из списка из списка"""

    element = chrome.find_element(By.XPATH, '//input')
    element.click()

    element.send_keys(other_things, Keys.ENTER)

    search_everywhere = chrome.find_element(By.XPATH, "//*[text()='Искать везде']")

    assert search_everywhere.is_enabled(), "Элемент не доступен"


@pytest.mark.double
def test_object_sale(chrome, web_page_phone):
    """находим элемент "Распродажа"  и проверяем что надпись скидки возле цены есть """

    element_sale = chrome.find_element(By.XPATH, "(//*[@class='a4226-a5'])[1]")
    element_sale.click()
    time.sleep(5)

    element_discount = chrome.find_elements(By.CSS_SELECTOR, "[class$='c3125-b1']")  # элементы скидок)

    assert element_sale.is_displayed(), 'элемент не работает'
    print("элемент включения распродажи доступен")

    for element in element_discount:
        assert element.is_displayed(), "элемент не виден"

    print("процент скидки виден")


@pytest.mark.maxim
def test_add_thing(chrome, web_page_phone):
    """"Добавляем элемент в корзину и проверяем иконку"""

    element_add_thing = chrome.find_element(By.XPATH, "(//*[@class='b235-a'])[4]")
    element_add_thing.click()

    element_thing = chrome.find_element(By.CSS_SELECTOR, "[href='/cart'] span:nth-child(1)")

    assert element_thing.is_displayed()


@pytest.mark.skip
def test_contacts(chrome, our_website):
    """идем вниз в строку и находим доп.инфор. об Ozon """

    element_is_help = chrome.find_element(By.CSS_SELECTOR, "[class='j0a d6p h8d']")

    chrome.execute_script("arguments[0].scrollIntoView();", element_is_help)
    element_under_house = chrome.find_elements(By.CSS_SELECTOR, "[class='d0i'] div:nth-child(1)")

    for element in element_under_house:
        assert element.is_enabled(), "no work"
        print(element.text)


@pytest.mark.regression
def test_location(chrome, our_website):
    """Открывается элемент(иконка) адреса доставки и доступ элемента Определить
    Местоположение"""

    street_element = chrome.find_element(By.CSS_SELECTOR, "[class='na6'] button:nth-child(1)")
    street_element.click()

    element_pickup = chrome.find_element(By.CSS_SELECTOR, "[class='zb6 z6b'] ")  # элемент самовывоз
    element_courier = chrome.find_element(By.CSS_SELECTOR, "[class='zb6'] ")  # элемент доставки курьером
    element_locate = chrome.find_element(By.CSS_SELECTOR, "[class='ga26-a undefined']")  # элемент "Определить
    # Местоположение"

    assert element_pickup.is_enabled(), "Element_pickup doesnt work"
    assert element_courier.is_enabled(), "Element_courier doesnt work"
    assert element_locate.is_enabled(), "Element_locate doesnt work"


@pytest.mark.xfail
def test_string_search_numbers(chrome, our_website):
    """В строке поиска вводим числовое значение из списка"""

    element = chrome.find_element(By.XPATH, '//input')
    element.click()

    element.send_keys("45", Keys.ENTER)

    search_everywhere = chrome.find_element(By.XPATH, "//*[text()='Искать везде']")

    assert search_everywhere.is_enabled(), "Элемент не доступен"
