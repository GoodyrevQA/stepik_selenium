'''https://stepik.org/lesson/228249/step/6?unit=200781'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    chb = browser.find_element(By.ID, "robotCheckbox")  #checkBox
    chb.click()

    rb = browser.find_element(By.ID, "robotsRule")  #radioButton
    browser.execute_script("return arguments[0].scrollIntoView(true);", rb) #выполняем JavaScript, скроллим до rb
    rb.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button) #выполняем JavaScript, скроллим до button

    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()