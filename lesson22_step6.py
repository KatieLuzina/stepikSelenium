from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим числа, чтобы посчитать сумму

    x = float(browser.find_element(by='id', value='input_value').text)
    res = math.log(abs(12*math.sin(x)))
    answer = browser.find_element(by='id', value='answer')
    answer.send_keys(res)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    check = browser.find_element(by='id', value='robotCheckbox')
    check.click()

    radio = browser.find_element(by='id', value='robotsRule')
    radio.click()

    button.click()


finally:
    # успеваем скопировать код за 30 секундf
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
