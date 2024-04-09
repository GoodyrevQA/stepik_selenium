'''https://stepik.org/lesson/237240/step/3'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        # этот тест запустится 2 раза

    def test_guest_should_see_navbar_element(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#language_selector")
        # этот тест тоже запустится дважды
'''pytest -s -v ./lesson3.6/test_lesson3_6_step3_param_class.py'''