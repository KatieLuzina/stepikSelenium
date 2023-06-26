from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим числа, чтобы посчитать сумму

    element1 = browser.find_element(by='id', value='num1')
    num1 = element1.text

    element2 = browser.find_element(by='id', value='num2')
    num2 = element2.text

    summ = int(num1) + int(num2)

    #Находим выпадающий список
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(summ))

    # Отправляем заполненную форму
    button = browser.find_element(by='css selector', value='button.btn')
    button.click()

finally:
    # успеваем скопировать код за 30 секундf
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
