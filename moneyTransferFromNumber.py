from selenium.common.exceptions import NoSuchElementException
from billing.billing_function import authorize
from selenium import webdriver
import time
import requests
from billing.billing_function import get_element
from selenium.webdriver.chrome.options import Options
import datetime

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/butovich_v/workspace/billingautotest/driver/chromedriver_lnx')

time.sleep(5)

authorize(driver, 'https://bill.bezlimit.ru/site/login', 'loginform-username', 'morozov_i', 'loginform-password', 'Takkurwatak1', '//*[@id="login-form"]/div[4]/div[2]/div[1]/button')

time.sleep(5)

driver.get(f'https://bill.bezlimit.ru/finance/plus/index?PlusSearch%5Bid%5D=&PlusSearch%5Bphone_number%5D=&PlusSearch%5Baccount_id%5D=&PlusSearch%5BanyPayment%5D=&PlusSearch%5Bdate%5D%5B0%5D=&PlusSearch%5Bdate%5D%5B1%5D=&PlusSearch%5Bdescription%5D=&PlusSearch%5Bpayment_category_id%5D=15&PlusSearch%5Bcreated%5D%5B0%5D={datetime.date.today()}&PlusSearch%5Bcreated%5D%5B1%5D=&PlusSearch%5Buser%5D=&PlusSearch%5Bpay_type%5D=&PlusSearch%5Bpay_system%5D=')

time.sleep(5)


def test(lst):
    return {a: lst.count(a) for a in set(lst) if lst.count(a) > 2}


def payment_sum(counter, summ, counter1):
    message_sum = ''
    while True:
        xpath_summa = '//*[@id="w0"]/table/tbody/tr[' + str(counter) + ']/td[4]'
        counter1 += 1
        try:
            element = driver.find_element_by_xpath(xpath_summa)
        except NoSuchElementException:
            break
        summa = int(get_element(driver, xpath_summa))
        summ += summa
        counter += 1
        message_sum = 'С номера ' + str(i) + ' перевели деньги более '+ str(counter1) + ' раз! Сумма переводов: ' + str(summ) + ' руб.!\n'
    return message_sum


def send_message(text: str):
    token = '1388568494:AAFZCASLFx64WZnpQLyqmBjht66Y3LU9xEI'
    url = "https://api.telegram.org/bot"
    channel_id = -1001178910709
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })


number_list = []

count1 = 1

while True:
    xpath_number = '//*[@id="w0"]/table/tbody/tr['+str(count1)+']/td[2]/a'
    try:
        element = driver.find_element_by_xpath(xpath_number)
    except NoSuchElementException:
        break
    number = str(get_element(driver, xpath_number))
    number_list.append(int(number))
    count1 += 1


fuck_number_list = test(number_list)

if fuck_number_list == {}:
    driver.quit()
else:
    message = f'\nВНИМАНИЕ!\nОбнаружены номера, с которых совершались множественные переводы!\n'

    count2 = 1
    total_sum = 0
    count3 = 0

    for i in set(fuck_number_list):
        driver.get(f'https://bill.bezlimit.ru/finance/plus/index?PlusSearch%5Bid%5D=&PlusSearch%5Bphone_number%5D='+str(i)+'&PlusSearch%5Baccount_id%5D=&PlusSearch%5BanyPayment%5D=&PlusSearch%5Bdate%5D%5B0%5D=&PlusSearch%5Bdate%5D%5B1%5D=&PlusSearch%5Bdescription%5D=&PlusSearch%5Bpayment_category_id%5D=15&PlusSearch%5Bcreated%5D%5B0%5D=' + str(datetime.date.today()) + '&PlusSearch%5Bcreated%5D%5B1%5D=&PlusSearch%5Buser%5D=&PlusSearch%5Bpay_type%5D=&PlusSearch%5Bpay_system%5D=')

        time.sleep(6)

        message += payment_sum(count2, total_sum, count3)

    print(message)

    send_message(message)

    driver.quit()
