#Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
from math import *

def func(y):
    return log(abs(12*sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    btn=browser.find_element_by_css_selector('.trollface').click()
    browser.switch_to.window(browser.window_handles[1])
    x=int(browser.find_element_by_css_selector('[id="input_value"]').text)
    inp=browser.find_element_by_css_selector('[id="answer"]').send_keys(str(func(x)))
    but=browser.find_element_by_css_selector('.btn').click()


finally:

    time.sleep(30)

    browser.quit()

