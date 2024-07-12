import time
import math
import pytest

link = "https://stepik.org/lesson/236895/step/1"
answer = math.log(int(time.time()))


@pytest.mark.parametrize('task_link', ["https://stepik.org/lesson/236895/step/1",
                                       "https://stepik.org/lesson/236896/step/1",
                                       "https://stepik.org/lesson/236897/step/1",
                                       "https://stepik.org/lesson/236898/step/1",
                                       "https://stepik.org/lesson/236899/step/1",
                                       "https://stepik.org/lesson/236903/step/1",
                                       "https://stepik.org/lesson/236904/step/1",
                                       "https://stepik.org/lesson/236905/step/1"
                                       ])
def test_login(browser, login_consts, task_link):
    browser.get(task_link)
    browser.implicitly_wait(5)
    login_button = browser.find_element(by='id', value='ember459')
    login_button.click()

    name_input = browser.find_element(by='name', value='login')
    name_input.send_keys(login_consts[0])

    password_input = browser.find_element(by='name', value='password')
    password_input.send_keys(login_consts[1])

    form_login_button = browser.find_element(by='css selector', value='button.sign-form__btn')
    form_login_button.click()

    time.sleep(5)

    my_time = math.log(int(time.time()))

    answer_input = browser.find_element(by='css selector', value='textarea.ember-text-area')
    answer_input.send_keys(my_time)

    confirm_button = browser.find_element(by='css selector', value='button.submit-submission')

    confirm_button.click()

    result = browser.find_element(by='css selector', value='p.smart-hints__hint')
    assert result.text == 'Correct!'
