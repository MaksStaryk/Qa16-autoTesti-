import time

import pytest
from selenium.webdriver import Keys

from locators.locators_for_main_page import *
from pages.main_page import MainPage
from conftest import driver_chrome
from list_words_and_number.words_and_number_list import list_other_think


@pytest.mark.title
def test_page(driver_chrome):
    page_main = MainPage(driver_chrome)
    page_main.open()

    assert page_main.title() == "OZON — интернет-магазин. Миллионы товаров по выгодным ценам", "Неправильно имя"


@pytest.mark.max
def test_find_element_seller(driver_chrome):
    """Нахождение элемента "Стать продавцом"  """

    seller = MainPage(driver_chrome)
    seller.open()

    assert seller.find_element_xpath(xpath_seller).is_displayed(), 'Элемент отсутствует'


# @pytest.mark.skip
def test_contacts(driver_chrome):
    """идем вниз  и находим QRCode Ozon """

    element_contacts = MainPage(driver_chrome)
    element_contacts.open()
    element_contacts.scroll_to_basement()

    assert element_contacts.find_element_xpath(basement_qrcode).is_displayed(), "Элемент отсутствует"

@pytest.mark.important
@pytest.mark.parametrize("other_things", list_other_think)
def test_search_string(driver_chrome, other_things):
    search = MainPage(driver_chrome)
    search.open()
    search.enter_world(other_things)

    assert search.find_element_xpath(element_search_every_where), "Element doesn't dispayed"
