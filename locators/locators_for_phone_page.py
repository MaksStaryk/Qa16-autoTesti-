from selenium.webdriver.common.by import By

# (By.XPATH, "") помощник для xpath
# (By.CSS_SELECTOR, ") помощник для css

button_doesnt_matter = (By.XPATH, "(//input[@class='e136-a0'])[1]")
checkbox = (By.XPATH, "(//div[@class='y9d'])[1]")
brand = (By.XPATH, "(//div[@class='ie7']//span)[2]")
three_days = (By.XPATH, "//span[contains(text(),'До 3 дней')]")
three_days_button = (By.XPATH, "(//span[@class='e136-a1'])[3]")
three_days_check = (By.XPATH, "(//input[@class='e136-a0'])[3]")
three_days_filter = (By.XPATH, "//span[text()='Сроки доставки: До 3 дней']")
add_basket_fir_element = (By.XPATH, "(//button[@class='f0 b237-a0 b237-b5 b237-a4'])[1]")
full_basket_1 = (By.XPATH, "//span[text()='1']")
empty_basket = (By.XPATH, "(//span[text()='0'])[4]")
clear_basket = (By.XPATH, "(//div[@class='f1 f2 f3 f5 si9'])//div[@class='ag17-a']")
original_phone = (By.XPATH, "(//*[@class='a4228-a2'])[7]")
button_original_phone = (By.XPATH, "(//label[contains(@class,'a4228-a a4228-a6')]//div)[4]")
text_original_thing = (By.XPATH, "(//b[text()='Оригинал'])[4]")
phone = (By.XPATH, "(//div[@class='f1 f3 f5 si9'])[1]")
search_string = (By.XPATH, "//input[@class='z3v tsBody500Medium']")
clear_search_string = (By.XPATH, "//div[@class='vz4']")
help_search = (By.CSS_SELECTOR, "[class='f153-a f153-a5 f153-b7']")
switch_to_phone = (By.XPATH, "//*[@class='r8i ir9'][1]")
buy_on_click = (By.CSS_SELECTOR, "[class='k3q kq7']")
vk_element = (By.XPATH, "//a[@title='VK']")
