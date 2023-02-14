from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    s1 = browser.find_element(By.ID, "num1")
    
    s2 = browser.find_element(By.ID, "num2") 

    s3 = str(int(s1.text) + int(s2.text))  #s1, s2 - web элементы, s1.text - значение
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(s3)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()