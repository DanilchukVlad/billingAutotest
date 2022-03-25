def get_element(driver, xpath):
    element = driver.find_element_by_xpath(xpath)

    element_num = element.text

    return element_num
