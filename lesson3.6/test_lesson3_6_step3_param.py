'''https://stepik.org/lesson/237240/step/3'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

'''pytest -s -v ./lesson3.6/test_lesson3_6_step3_param.py'''