from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time



try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    name1.send_keys("Иван")

    name2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    name2.send_keys("Гудырев")

    mail = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    mail.send_keys("mail@mail.mail")

    our_file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__)) #определяем путь к нашей текущей папке
    file_path = os.path.join(current_dir, 'file.txt') #добавляем в путь файл
    our_file.send_keys(file_path) #посылаем файл

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()