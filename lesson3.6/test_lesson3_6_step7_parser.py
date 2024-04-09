'''https://stepik.org/lesson/237240/step/7?unit=209628'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

'''
pytest -s -v ./lesson3.6/test_lesson3_6_step7_parser.py
pytest -s -v --browser_name=chrome ./lesson3.6/test_lesson3_6_step7_parser.py
pytest -s -v --browser_name=firefox ./lesson3.6/test_lesson3_6_step7_parser.py


'''