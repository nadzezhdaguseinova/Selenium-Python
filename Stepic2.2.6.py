
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

#прокрутить до искомой кнопки
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(30)
    browser.quit()



