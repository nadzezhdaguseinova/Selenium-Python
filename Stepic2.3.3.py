from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button=browser.find_element_by_tag_name("button.btn")
    button.click()

    # закрыть всплывающее окно
    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()





#alert = browser.switch_to.alert             #Для этого нужно сначала переключиться на окно с alert,
#alert.accept()                # а затем принять его с помощью команды accept():
#alert = browser.switch_to.alert        # получить текст из  alert
#alert_text = alert.text



