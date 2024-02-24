from selenium.webdriver.common.by import By

# (By.XPATH, "")

button_doesnt_matter = (By.XPATH, "(//input[@class='e136-a0'])[1]")
checkbox = (By.XPATH, "(//div[@class='y9d'])[1]")
brand = (By.XPATH, "(//div[@class='ie7']//span)[2]")
three_days = (By.XPATH, "//span[contains(text(),'До 3 дней')]")
three_days_button = (By.XPATH, "(//input[@class='e136-a0'])[2]")
three_days_filter = (By.XPATH, "//span[text()='Сроки доставки: До 3 дней']")
add_basket_fir_element = (By.XPATH, "(//div[@class='b237-a'])[3]")
full_basket_1 = (By.XPATH, "//span[text()='1']")
clear_basket = (By.XPATH, "(//button[@class='ag17-a0 ag17-a7']//div)[1]")
original_phone = (By.XPATH, "(//*[@class='a4228-a2'])[7]")
button_original_phone = (By.XPATH, "(//label[contains(@class,'a4228-a a4228-a6')]//div)[4]")
text_orinal_thing = (By.XPATH, "(//b[text()='Оригинал'])[4]")