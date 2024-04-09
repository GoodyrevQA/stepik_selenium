'''https://stepik.org/lesson/237240/step/8?unit=209628'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")

'''Чтобы указать количество перезапусков для каждого из упавших тестов, нужно добавить в командную строку параметр:
"--reruns n", где n — это количество перезапусков. 
Если при повторных запусках тесты пройдут успешно, то и прогон тестов будет считаться успешным. 
Количество перезапусков отображается в отчёте, благодаря чему можно позже анализировать проблемные тесты.
Дополнительно мы указали параметр "--tb=line", чтобы сократить лог с результатами теста.

pytest -v --tb=line --reruns 1 --browser_name=chrome ./lesson3.6/test_lesson3_6_step8_rerun.py
'''