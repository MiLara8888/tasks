# этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from math import *

def func(y):
    return log(abs(12*sin(y)))

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button=browser.find_element_by_css_selector('[id="book"]')
    browser.execute_script('window.scrollBy(0,150);')
    n=WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()
    x=int(browser.find_element_by_css_selector('[id="input_value"]').text)
    x=str(func(x))
    browser.execute_script('window.scrollBy(0,450);')
    inp=browser.find_element_by_css_selector('[id="answer"]').send_keys(x)
    btn=browser.find_element_by_css_selector('[id="solve"]').click()




finally:

    time.sleep(10)

    browser.quit()

