from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # говорим WebDriver ждать все элементы в течение 5 секунд
    #browser.implicitly_wait(5)

    book = browser.find_element(By.ID, "book")
    price = WebDriverWait(browser,11).until(
        EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
    book.click()

    x_element =browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    solve = browser.find_element(By.ID,"solve")
    solve.click()

finally:
    time.sleep(30)
    browser.quit()


