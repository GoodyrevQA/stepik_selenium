from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    


    # Ваш код, который заполняет обязательные поля
    chest = browser.find_element(By.ID, "treasure")  # находим сундук

    x = chest.get_attribute("valuex")
    y = calc(x)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    input2 = browser.find_element(By.ID, "robotCheckbox") 
    input2.click()
    input3 = browser.find_element(By.ID, "robotsRule")
    input3.click()

    time.sleep(1)
  

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()