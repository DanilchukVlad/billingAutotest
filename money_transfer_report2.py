from billing.billing_function import authorize
from selenium import webdriver
import time
import requests
from billing.locators.report2 import xpath_column_remittance
from billing.billing_function import get_element
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/butovich_v/workspace/billingautotest/driver/chromedriver_lnx')

time.sleep(5)

authorize(driver, 'https://bill.bezlimit.ru/site/login', 'loginform-username', 'morozov_i', 'loginform-password', 'Takkurwatak1', '//*[@id="login-form"]/div[4]/div[2]/div[1]/button')

time.sleep(5)

driver.get('https://bill.bezlimit.ru/report/monitoring')


def send_message(text: str):
    token = '1388568494:AAFZCASLFx64WZnpQLyqmBjht66Y3LU9xEI'
    url = "https://api.telegram.org/bot"
    channel_id = -1001414238186
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })


payments = str(get_element(driver, xpath_column_remittance))

if get_element(driver, xpath_column_remittance) >= 50:

    channel_id = -1001414238186

    message = f'\nВНИМАНИЕ!\nПодозрительная активность при переводе средств с номера на номер!\n' \
              f'Сумма уже: {payments} руб!'

    send_message(message)

driver.quit()
