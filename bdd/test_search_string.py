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


@given("that I have a web browser")
def step_given(driver_chrome):
    driver_chrome.driver = webdriver.Chrome()


@when("I open the home page")
def step_when(driver_chrome):
    driver_chrome.get("https://5element.by")


@then("I should see the search bar")
def step_then(driver_chrome):
    assert driver_chrome.find_element_by_name("q")
