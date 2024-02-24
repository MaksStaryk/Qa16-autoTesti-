from selenium.webdriver.common.by import By

xpath_seller = (By.XPATH, "//a[@class='aj7 s5d ds6']")
xpath_seller1 = (By.PARTIAL_LINK_TEXT, "Стать продавцом")
search_string = (By.XPATH, "//input")
element_basement = (By.XPATH, "//*[@class='aj7 dh9']")
basement_qrcode = (By.XPATH, "(//*[@class='g3d b957-a'])")
element_search_every_where = (By.XPATH, "//*[text()='Искать везде']")
"""элемент 'вход'"""
acess = (By.XPATH, "(//*[@class='dh5'])/div[1]")
"""элемент 'выбрать на карте'"""
select_on_the_map = (By.CSS_SELECTOR, "[class='b237-a0 b237-b2 b237-a4']")
"""элемент самовывоз """
element_pickup = (By.CSS_SELECTOR, "[class='b0y']  button:nth-child(1)")
"""элемент доставки курьером"""
element_courier = (By.CSS_SELECTOR, "[class='b0y']  button:nth-child(2)")
"""элемент "Определить Местоположение"""
element_locate = (By.CSS_SELECTOR, "[class='ga28-a undefined'] ")
"""элемент 'Укажите адрес доставки'"""
delivery_address = (By.XPATH, "(//div[@class='ga28-a2 tsBodyControl400Small'])[3]")
"""элемент строки ввода номера"""
num_string = (By.CSS_SELECTOR, "[class='d215-a d215-a3 wa8b d215-a4']")
"""элемент поисковой строки"""
search = (By.CSS_SELECTOR, "[action='/search'] div:nth-child(1) div:nth-child(2)")
"""element avtorization"""
element_access = (By.CSS_SELECTOR, "[data-widget='profileMenuAnonymous']")
element_access_2 = (By.CSS_SELECTOR, "div[class='aj7 do5'] span[class='od5']")
things = (By.XPATH, "(//li[@class='h6d']//a)[5]")
basket =(By.XPATH, "//div[@class='ace0']//div[1]//div[2]//div[1]//div[1]//button[1]//div[2]")
catalog = (By.XPATH, "//button[@class='b237-a0 b237-b5']//div[@class='b237-a']")
web_site = "https://seller.ozon.ru/?utm_source=ozonru_web&utm_medium=link&utm_campaign=header_nachat_prodavat_na_ozon/"
product_food = (By.XPATH, "(//li[@class='h6d']//a)[5]")
search_button = (By.XPATH, "//div[@class='ag17-a']")
copy_search_every = (By.XPATH, "//span[contains(text(),'Искать везде')]")









