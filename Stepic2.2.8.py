from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)

    FirstName = browser.find_element_by_name("firstname")
    FirstName.send_keys("z")
    LastName = browser.find_element_by_name("lastname")
    LastName.send_keys("z")
    email = browser.find_element_by_name("email")
    email.send_keys("z")


    current_dir = os.path.abspath(os.path.dirname(__file__))
    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, "text.txt")
    # добавляем к этому пути имя файла
    file1 = browser.find_element_by_id("file")
    file1.send_keys("C:\\Users\\User\\.PyCharmCE2019.2\\config\\scratches\\text.txt")

#    print(os.path.abspath(__file__))
#    print(os.path.abspath(os.path.dirname(__file__)))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

