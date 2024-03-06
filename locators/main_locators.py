from selenium.webdriver.common.by import By


class MainLocators:
    XPATH_SELLER = (By.XPATH, "//a[@class='aj7 s5d ds6']")
    XPATH_SELLER1 = (By.PARTIAL_LINK_TEXT, "Стать продавцом")
    SEARCH_STRING = (By.XPATH, "//input")
    ELEMENT_BASEMENT = (By.XPATH, "//*[@class='aj7 dh9']")
    BASEMENT_QRCODE = (By.XPATH, "(//*[@class='g3d b957-a'])")
    ELEMENT_SEARCH_EVERY_WHERE = (By.XPATH, "//*[text()='Искать везде']")
    """элемент 'вход'"""
    ACESS = (By.XPATH, "(//*[@class='dh5'])/div[1]")
    """элемент 'выбрать на карте'"""
    SELECT_ON_THE_MAP = (By.CSS_SELECTOR, "[class='b237-a0 b237-b2 b237-a4']")
    """элемент самовывоз """
    ELEMENT_PICKUP = (By.CSS_SELECTOR, "[class='b0y']  button:nth-child(1)")
    """элемент доставки курьером"""
    ELEMENT_COURIER = (By.CSS_SELECTOR, "[class='b0y']  button:nth-child(2)")
    """элемент "Определить Местоположение"""
    ELEMENT_LOCATE = (By.CSS_SELECTOR, "[class='ga28-a undefined'] ")
    """элемент 'Укажите адрес доставки'"""
    DELIVERY_ADDRESS = (By.XPATH, "(//div[@class='ga28-a2 tsBodyControl400Small'])[3]")
    """элемент строки ввода номера"""
    NUM_STRING = (By.CSS_SELECTOR, "[class='d215-a d215-a3 wa8b d215-a4']")
    """элемент поисковой строки"""
    SEARCH = (By.CSS_SELECTOR, "[action='/search'] div:nth-child(1) div:nth-child(2)")
    """element avtorization"""
    ELEMENT_ACCESS = (By.CSS_SELECTOR, "[data-widget='profileMenuAnonymous']")
    ELEMENT_ACCESS_2 = (By.CSS_SELECTOR, "div[class='aj7 do5'] span[class='od5']")
    THINGS = (By.XPATH, "(//li[@class='h6d']//a)[5]")
    BASKET = (By.XPATH, "//div[@class='ace0']//div[1]//div[2]//div[1]//div[1]//button[1]//div[2]")
    CATALOG = (By.XPATH, "//button[@class='b237-a0 b237-b5']//div[@class='b237-a']")
    WEB_SITE = "https://seller.ozon.ru/?utm_source=ozonru_web&utm_medium=link&utm_campaign=header_nachat_prodavat_na_ozon/"
    PRODUCT_FOOD = (By.XPATH, "(//li[@class='h6d']//a)[5]")
    SEARCH_BUTTON = (By.XPATH, "//div[@class='ag17-a']")
    COPY_SEARCH_EVERY = (By.XPATH, "//span[contains(text(),'Искать везде')]")
