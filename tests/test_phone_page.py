import time
import pytest

from random import randint

from locators.locators_for_phone_page import *
from pages.main_page import MainPage
from conftest import driver_chrome

from pages.phone_page import PhonePage


@pytest.mark.title
def test_title(driver_chrome):
    title = PhonePage(driver_chrome)
    title.open_phone_page()

    assert title.title() == "Телефоны – купить смартфон на OZON по низкой цене", "title is wrong"


def test_delivery_terms(driver_chrome):
    """В Сроки доставки по-умолчанию стоит Неважно"""

    delivery = PhonePage(driver_chrome)
    delivery.open_phone_page()

    assert delivery.find_element(button_doesnt_matter).is_selected, "element not selected"


def test_get_text_brand(driver_chrome):
    """на странице есть текст Бренды"""

    brand_text = PhonePage(driver_chrome)
    brand_text.open_phone_page()

    assert brand_text.get_text(brand) == "Бренды"


def test_selected_3_days(driver_chrome):
    """кликаем на элемент 3 дня"""

    selected = PhonePage(driver_chrome)
    selected.open_phone_page()
    selected.find_element(three_days)
    selected.click_three_days()
    time.sleep(1)

    assert selected.get_attribute(three_days_button, "value") == 'true', "element not equal true"
    assert selected.find_element(three_days_filter).is_displayed, "element not displayed"


def test_add_to_basket(driver_chrome):
    """Добавляем товар в корзину """

    basket = PhonePage(driver_chrome)
    basket.open_phone_page()
    basket.find_element(add_basket_fir_element)
    basket.click_add_basket()
    time.sleep(4)

    assert basket.find_element(full_basket_1).is_displayed, "element not displayed"
    assert basket.get_text(full_basket_1) == "1", "element not equal 1"


def test_clear_basket(driver_chrome):
    """удаляем товар из корзины"""

    basket = PhonePage(driver_chrome)
    basket.open_phone_page()
    basket.find_element(add_basket_fir_element)
    basket.click_add_basket()
    time.sleep(2)
    basket.click_clear_basket()
    time.sleep(2)

    assert basket.get_text(full_basket_1) is None, 'element equal1'


def test_selected_phone(driver_chrome):
    phone = PhonePage(driver_chrome)
    phone.open_phone_page()
    phone.scroll_to_basement(brand)
    phone.click_original_phone()

    assert phone.find_element(text_orinal_thing).is_displayed, 'orignal name not displayed'

