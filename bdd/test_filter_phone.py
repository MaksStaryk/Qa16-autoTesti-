import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import given, when, then


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@given("the user is on the phone page")
def step_given(driver_chrome):
    driver_chrome.get("https://5element.by/catalog/smartfony/")


@when("the user scrolls to the brand section")
def step_when(driver_chrome):
    brand_section = driver_chrome.find_element_by_xpath("//div[@data-filter-name='Бренд']")
    driver_chrome.execute_script("arguments[0].scrollIntoView();", brand_section)


@when("the user selects the original product filter")
def step_when(driver_chrome):
    original_product_filter = driver_chrome.find_element_by_xpath("//span[text()='Оригинальный товар']")
    original_product_filter.click()


@then("the user should see the original product text displayed on the page")
def step_then(driver_chrome):
    original_product_text = driver_chrome.find_element_by_xpath("//span[text()='Оригинальный товар']")
    assert original_product_text.is_displayed(), 'orignal name not displayed'
