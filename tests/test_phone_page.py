import time
import pytest

from conftest import driver_chrome
from pages.phone_page import PhonePage
from locators.phone_locators import PhonePageLocator


@pytest.mark.title
def test_title(driver_chrome):
    title = PhonePage(driver_chrome)
    title.open_phone_page()

    assert title.title() == "Телефоны – купить смартфон на OZON по низкой цене", "title is wrong"


def test_delivery_terms(driver_chrome):
    """В Сроки доставки по-умолчанию стоит Неважно"""

    delivery = PhonePage(driver_chrome)
    delivery.open_phone_page()

    assert delivery.find_element(PhonePageLocator.BUTTON_DOESNT_MATTER).is_selected, "element not selected"


def test_get_text_brand(driver_chrome):
    """на странице есть текст Бренды"""

    brand_text = PhonePage(driver_chrome)
    brand_text.open_phone_page()

    assert brand_text.get_text(PhonePageLocator.BRAND) == "Бренды"


def test_selected_3_days(driver_chrome):
    """кликаем на элемент 3 дня"""

    selected = PhonePage(driver_chrome)
    selected.open_phone_page()
    selected.find_element(PhonePageLocator.THREE_DAYS)
    selected.click_three_days()
    time.sleep(3)

    assert selected.get_attribute(PhonePageLocator.THREE_DAYS_CHECK, "value") == 'true', "element not equal true"
    assert selected.find_element(PhonePageLocator.THREE_DAYS_FILTER).is_displayed, "element not displayed"


def test_add_to_basket(driver_chrome):
    """Добавляем товар в корзину """

    basket = PhonePage(driver_chrome)
    basket.open_phone_page()
    basket.click_add_basket(PhonePageLocator.PHONE)
    time.sleep(4)

    assert basket.find_element(PhonePageLocator.FULL_BASKET_1).is_displayed, "element not displayed"
    assert basket.get_text(PhonePageLocator.FULL_BASKET_1) == "1", "element not equal 1"


def test_clear_basket(driver_chrome):
    """удаляем товар из корзины"""

    basket = PhonePage(driver_chrome)
    basket.open_phone_page()
    time.sleep(2)
    basket.click_add_basket(PhonePageLocator.PHONE)
    time.sleep(2)
    basket.click_test(PhonePageLocator.CLEAR_BASKET)
    time.sleep(2)

    assert basket.get_text(PhonePageLocator.EMPTY_BASKET) is "0", 'element equal1'


def test_selected_phone(driver_chrome):
    """выбираем Оргигинальный товар"""

    phone_selec = PhonePage(driver_chrome)
    phone_selec.open_phone_page()
    phone_selec.scroll_to_basement(PhonePageLocator.BRAND)
    phone_selec.click_original_phone()

    assert phone_selec.find_element(PhonePageLocator.TEXT_ORIGINAL_THING).is_displayed, 'orignal name not displayed'


def test_clear_string(driver_chrome):
    """Заполняем поле и удaляем содержимое"""

    clear_string = PhonePage(driver_chrome)
    clear_string.open_phone_page()
    clear_string.clear_text('Dell', PhonePageLocator.SEARCH_STRING)

    assert not clear_string.find_element(PhonePageLocator.CLEAR_SEARCH_STRING).is_displayed, "we see text"


@pytest.mark.xfail
def test_select(driver_chrome):
    """Выбираем в выподаещем списке """

    some_select = PhonePage(driver_chrome)
    some_select.open_phone_page()
    some_select.select_some(PhonePageLocator.HELP_SEARCH, "Высокий рейтинг")


def test_switch_to(driver_chrome):
    """"переходим по ссылке во вторую вкладку"""
    switch_to = PhonePage(driver_chrome)
    switch_to.open_phone_page()

    assert switch_to.switch_to_page(PhonePageLocator.VK_ELEMENT) == "https://vk.com/ozon?perehod=footer", (
        "the transition was not completed")
