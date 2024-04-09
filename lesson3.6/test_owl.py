from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from pytest import mark
from time import time
from math import log
import password

message = ''


@mark.parametrize('lesson', ['895', '896', '897', '898', '899', '903', '904', '905'])
def test_parametrize_stepik(browser, lesson):
    global message
    link = f'https://stepik.org/lesson/236{lesson}/step/1'
    browser.get(link)

    # авторизовываемся перед тем, как производить какие-либо действия
    browser.find_element(By.CLASS_NAME, 'navbar__auth_login').click()  # нажимаем кнопку Войти в навбаре
    email = browser.find_element(By.ID, 'id_login_email')
    email.send_keys(password.EMAIL) 
    password = browser.find_element(By.ID, 'id_login_password')
    password.send_keys(password.PASSWORD) 
    browser.find_element(By.CLASS_NAME, 'button_with-loader').click()  # нажимаем кнопку Войти в окне авторизации

    # после авторизации проверяем есть ли кнопка решить снова/сброса и если есть, то очищаем поле для ответа
    try:
        browser.find_element(By.CLASS_NAME, 'again-btn').click()  # нажимаем кнопку решить снова или сброса
    except NoSuchElementException:
        pass
    try:
        browser.find_element(By.XPATH, '//*[text()="OK"]').click()  # нажимаем ОК, если вылетает окно очистки поля
    except NoSuchElementException:
        pass

    textarea = browser.find_element(By.CLASS_NAME, 'textarea')  # находим поле для ответа
    textarea.send_keys(log(int(time())))  # в поле для ответа вводим решение по формуле, считая "налету"
    browser.find_element(By.CLASS_NAME, 'submit-submission:enabled').click()  # нажимаем кнопку, когда она активна
    feedback_text = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint').text  # находим текст в черном поле

    message += feedback_text if feedback_text != 'Correct!' else ''  # собираем сообщение из кусочков посланий :)

    assert feedback_text == 'Correct!', message  # в последнем упавшем тесте будет итоговое послание в AssertionError ;)

'''pytest -s -v ./lesson3.6/test_owl.py'''