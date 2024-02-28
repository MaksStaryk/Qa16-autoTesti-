from selenium.webdriver.common.by import By


class LocatorPhonePage:
    BUTTON_DOESNT_MATTER = (By.XPATH, "(//input[@class='e136-a0'])[1]")
    CHECKBOX = (By.XPATH, "(//div[@class='y9d'])[1]")
    BRAND = (By.XPATH, "(//div[@class='ie7']//span)[2]")
    THREE_DAYS = (By.XPATH, "//span[contains(text(),'До 3 дней')]")
    THREE_DAYS_BUTTON = (By.XPATH, "(//span[@class='e136-a1'])[3]")
    THREE_DAYS_CHECK = (By.XPATH, "(//input[@class='e136-a0'])[3]")
    THREE_DAYS_FILTER = (By.XPATH, "//span[text()='Сроки доставки: До 3 дней']")
    ADD_BASKET_FIR_ELEMENT = (By.XPATH, "(//button[@class='f0 b237-a0 b237-b5 b237-a4'])[1]")
    FULL_BASKET_1 = (By.XPATH, "//span[text()='1']")
    EMPTY_BASKET = (By.XPATH, "(//span[text()='0'])[4]")
    CLEAR_BASKET = (By.XPATH, "(//div[@class='f1 f2 f3 f5 si9'])//div[@class='ag17-a']")
    ORIGHINAL_PHONE = (By.XPATH, "(//*[@class='a4228-a2'])[7]")
    BUTTON_ORIGINAL_PHONE = (By.XPATH, "(//label[contains(@class,'a4228-a a4228-a6')]//div)[4]")
    TEXT_ORIGINAL_THING = (By.XPATH, "(//b[text()='Оригинал'])[4]")
    PHONE = (By.XPATH, "(//div[@class='f1 f3 f5 si9'])[1]")
    SEARCH_STRING = (By.XPATH, "//input[@class='z3v tsBody500Medium']")
    CLEAR_SEARCH_STRING = (By.XPATH, "//div[@class='vz4']")
    HELP_SEARCH = (By.CSS_SELECTOR, "[class='f153-a f153-a5 f153-b7']")
    SWITHC_TO_PHONE = (By.XPATH, "//*[@class='r8i ir9'][1]")
    BUY_ON_CLICK = (By.CSS_SELECTOR, "[class='k3q kq7']")
    VK_ELEMENT = (By.XPATH, "//a[@title='VK']")
