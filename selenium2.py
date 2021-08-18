#В данной задаче вам нужно будет снова преодолеть капчу для роботов и
# справиться с ужасным и огромным футером, который дизайнер всё никак не успевает переделать.
# Вам потребуется написать код, чтобы:
# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
from math import *

def calk(y):
    return log(abs(12*sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    x=int(browser.find_element_by_css_selector('[id="input_value"]').text)
    y=calk(x)
    browser.execute_script("window.scrollBy(0, 130);")
    inp=browser.find_element_by_css_selector('[id="answer"]')
    inp.send_keys(str(y))
    rad=browser.find_element_by_css_selector('[id="robotCheckbox"]').click()
    rob=browser.find_element_by_css_selector('[id="robotsRule"]').click()
    btn=browser.find_element_by_css_selector('.btn').click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла