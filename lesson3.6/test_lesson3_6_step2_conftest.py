'''https://stepik.org/lesson/193188/step/5'''

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    print()
    print("Используем фикстуру из Conftest")
    print()
    browser.find_element(By.CSS_SELECTOR, "#login_link")

'''pytest -s -v ./lesson3.6/test_lesson3_6_step2_conftest.py'''