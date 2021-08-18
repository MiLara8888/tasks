from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
from math import *
import os
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого скрипта
file_name = "numbers.txt"     # имя файла, который будем загружать на сайт
file_path = os.path.join(current_dir, file_name)      # получаем путь к загружаемому файлу
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    name=browser.find_element_by_css_selector("[placeholder='Enter first name']").send_keys('Lara')
    last=browser.find_element_by_css_selector("[placeholder='Enter last name']").send_keys('Mir')
    mail = browser.find_element_by_css_selector("[placeholder='Enter email']").send_keys('Mir@mail')
    file=browser.find_element_by_css_selector('[id="file"]').send_keys(file_path)           # отправляем файл
    btn=browser.find_element_by_css_selector('.btn').click()

finally:

    time.sleep(30)

    browser.quit()

