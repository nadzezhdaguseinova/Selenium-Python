from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link="http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    n1 = int(num1.text)
    num2 = browser.find_element_by_id("num2")
    n2 = int(num2.text)
    n3 = (int(n1) + int(n2))

    browser.find_element_by_id("dropdown").click()
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(n3))

    #x =val.get_attribute(str(n3))

    #select.select_by_visible_text(n3)
    #select.find_element_by_value(n3).click()
    #browser.find_element_by_css_selector("[value=" + n3 +"]").click()


    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
