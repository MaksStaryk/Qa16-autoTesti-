from selenium.webdriver.common.by import By


class PageLocators:

    BECOME_IS_SELLER = (By.LINK_TEXT, "Стать продавцом")
    STRING_SEARCH = (By.XPATH, '//input')
    CLOTHEST_AND_SHOES = (By.LINK_TEXT, "Одежда и обувь")
    BASKET = (By.CSS_SELECTOR, "a[href='/cart'")