import time
import datetime as dt


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


def get_element_string(driver, xpath):
    element = driver.find_element_by_xpath(xpath)

    element_num = element.text

    return element_num


def calculate_time_difference(time_delta=30, read_time="1980-01-01 00:00:00",
                                  date_format='%Y-%m-%d %H:%M:%S', days=False):
    """
    It is function for calculate difference between two values of date-time.
    :param time_delta:
    :param read_time:
    :param date_format:
    :param days:
    :return:
    """
    if not days:
        now = dt.datetime.now()
        delta = dt.timedelta(minutes=time_delta)
    else:
        now = dt.datetime.today()
        delta = dt.timedelta(days=time_delta)
    read_time = dt.datetime.strptime(read_time, date_format)
    if now-read_time > delta:
        return True
    else:
        return False
