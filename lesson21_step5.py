from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(by='id', value='input_value')
    x = x_element.text

    y = calc(x)
    answer_el = browser.find_element(by='id', value='answer')
    answer_el.send_keys(y)

    robot_check = browser.find_element(by='id', value='robotCheckbox')
    robot_radio = browser.find_element(by='id', value='robotsRule')

    robot_check.click()
    robot_radio.click()

    button = browser.find_element(by='css selector', value="button.btn")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
