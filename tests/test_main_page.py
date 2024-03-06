import time
import pytest

from random import randint
from locators.main_locators import MainLocators
from pages.main_page import MainPage
from conftest import driver_chrome
from list_words_and_number.words_and_number_list import list_other_think


@pytest.mark.title
def test_page(driver_chrome):
    """корректность title на страницы"""

    page_main = MainPage(driver_chrome)
    page_main.open()

    assert page_main.title() == "OZON — интернет-магазин. Миллионы товаров по выгодным ценам", "Неправильно имя"


@pytest.mark.max
def test_find_element_seller(driver_chrome):
    """Нахождение элемента "Стать продавцом"  """

    seller = MainPage(driver_chrome)
    seller.open()

    assert seller.find_element(MainLocators.XPATH_SELLER).is_enabled(), 'Элемент отсутствует'


# pytest.mark.skip
def test_qr(driver_chrome):
    """идем вниз  и находим QRCode Ozon """

    element_qr = MainPage(driver_chrome)
    element_qr.open()
    element_qr.scroll_to_basement(MainLocators.BASEMENT_QRCODE)
    time.sleep(3)

    assert element_qr.find_element(MainLocators.BASEMENT_QRCODE).is_displayed(), "Элемент отсутствует"


@pytest.mark.important
@pytest.mark.parametrize("other_things", list_other_think)
def test_search_string(driver_chrome, other_things):
    """В строке поиска вводим названия предметов из списка"""

    search_str = MainPage(driver_chrome)
    search_str.enter_world(other_things)

    assert search_str.find_element(MainLocators.ELEMENT_SEARCH_EVERY_WHERE), "Element doesn't dispayed"


@pytest.mark.xfail
def test_test_string_search_numbers(driver_chrome):
    """В строке поиска вводим числовое значение из списка"""

    search = MainPage(driver_chrome)
    search.open()
    search.enter_number(randint(1, 198))

    assert search.find_element(MainLocators.ELEMENT_SEARCH_EVERY_WHERE), "Element doesn't dispayed"


@pytest.mark.map
def test_location(driver_chrome):
    """кликаем по Укажите адрес доставки"""

    street_element = MainPage(driver_chrome)
    street_element.open()
    street_element.location()

    assert street_element.find_element(MainLocators.DELIVERY_ADDRESS).is_displayed, "element not dispalayed"
    assert street_element.find_element(MainLocators.ELEMENT_PICKUP).is_enabled(), "element not available"
    assert street_element.find_element(MainLocators.ELEMENT_COURIER).is_enabled(), "element not available"
    assert street_element.find_element(MainLocators.ELEMENT_LOCATE).is_enabled(), "element not available"


def test_check_search_string(driver_chrome):
    """корректность работы строки Поиск"""
    search_str = MainPage(driver_chrome)
    search_str.open()
    search_str.search_string('iphone')

    assert "iphone - купить на OZON" == search_str.title()


def test_add_basket(driver_chrome):
    """кликаем по элементу Продукты питания """

    add_basket = MainPage(driver_chrome)
    add_basket.open()
    add_basket.food()
    time.sleep(6)

    assert 'Продукты питания' in add_basket.title(), "element not dispalayed"


def test_text_catalog(driver_chrome):
    """check text """

    catalog_text = MainPage(driver_chrome)
    if catalog_text.get_text(MainLocators.DELIVERY_ADDRESS) is not None:
        assert "Каталог" in catalog_text.get_text(MainLocators.DELIVERY_ADDRESS)
    else:
        print("element doesn't find")


def test_get_attribute(driver_chrome):
    """element attribute corresponds to page link"""

    attribute = MainPage(driver_chrome)
    attribute.open()

    assert attribute.get_attribute(MainLocators.XPATH_SELLER, "href") == MainLocators.WEB_SITE, "href is wrong"


def test_get_text(driver_chrome):
    """get element text"""
    get_text = MainPage(driver_chrome)
    get_text.open()

    assert get_text.get_text(MainLocators.PRODUCT_FOOD) == "Продукты питания", "text is wrong"


def test_submit(driver_chrome):
    submit = MainPage(driver_chrome)
    submit.open()
    submit.find_element(MainLocators.SEARCH_STRING)
    submit.search_field("Nokia 3310")
    submit.submit(MainLocators.SEARCH_BUTTON)

    assert submit.find_element(MainLocators.COPY_SEARCH_EVERY), "submit doesnt work"


def test_send(driver_chrome):
    """"""
    send = MainPage(driver_chrome)
    send.open()
    send.enter_text(MainPage.SEARCH_STRING, "iphone")
    time.sleep(1)
    send.enter_keyboard(MainPage.SEARCH_STRING)

    assert send.find_element(MainLocators.ELEMENT_SEARCH_EVERY_WHERE).is_displayed, "element everywhere not displayed"


def test_move(driver_chrome):
    move = MainPage(driver_chrome)
    move.open()
    move.mouse_move(MainLocators.DELIVERY_ADDRESS)
    time.sleep(5)