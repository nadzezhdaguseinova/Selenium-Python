from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("option:nth-child(2)").click()
# Последняя строчка может выглядеть и так:

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value("1")
    # ищем элемент с текстом "Python"
    # select.select_by_visible_text("text")  ищет элемент по видимому тексту
    # select.select_by_index(index).

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
