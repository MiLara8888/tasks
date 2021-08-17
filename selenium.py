

#Открыть страницу http://suninjuly.github.io/get_attribute.html.
#Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
#Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
#Посчитать математическую функцию от x (сама функция остаётся неизменной).
#Ввести ответ в текстовое поле.
#Отметить checkbox "I'm the robot".
#Выбрать radiobutton "Robots rule!".
#Нажать на кнопку "Submit".


from selenium import webdriver
import time
from math import *

def calc(x):
  return str(log(abs(12*sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    ht=browser.find_element_by_css_selector("[id='treasure']")
    n=ht.get_attribute('valuex')
    n=int(n)
    y=calc(n)
    inp=browser.find_element_by_css_selector('[id="answer"]')
    inp.send_keys(y)
    box=browser.find_element_by_css_selector('[id="robotCheckbox"]')
    box.click()
    radio=browser.find_element_by_css_selector('[id="robotsRule"]')
    radio.click()
    button=browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла