from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(by='name', value='firstname')
    input1.send_keys("Katya")

    input2 = browser.find_element(by='name', value='lastname')
    input2.send_keys("Paga")

    input3 = browser.find_element(by='name', value='email')
    input3.send_keys("test@mail.com")

    file_button = browser.find_element(by='id', value='file')
    #file_button.click()

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    file_button.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    # успеваем скопировать код за 30 секундf
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
