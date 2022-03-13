import time


def authorize(driver, adress, login_path, login, password_path, password, button):
    driver.get(adress)

    time.sleep(7)

    login_input = driver.find_element_by_id(login_path)

    login_input.send_keys(login)

    password_input = driver.find_element_by_id(password_path)

    password_input.send_keys(password)

    button_enter = driver.find_element_by_xpath(button)

    button_enter.click()


def get_element(driver, xpath):
    element = driver.find_element_by_xpath(xpath)

    element_num = float(element.text)

    element_num = abs(int(element_num))

    return element_num
