import time

from billing.billing_function import get_element_string
from billing.billing_function import authorize
from billing.billing_function import calculate_time_difference

from telegram_pack.send_telegram import send_to_telegram

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/butovich_v/workspace/billingautotest/driver/chromedriver_lnx')

driver.get('https://bill.bezlimit.ru/finance/accrual?AccrualSearch%5Bid%5D=&AccrualSearch%5Bphone_number%5D=&AccrualSearch%5BtariffId%5D=&AccrualSearch%5Baccount_id%5D=&AccrualSearch%5Bamount%5D=&AccrualSearch%5Bdate%5D%5B0%5D=&AccrualSearch%5Bdate%5D%5B1%5D=&AccrualSearch%5Bdate_end%5D%5B0%5D=&AccrualSearch%5Bdate_end%5D%5B1%5D=&AccrualSearch%5Bfeature_id%5D=&AccrualSearch%5Bdescription%5D=&AccrualSearch%5Bminus_category_id%5D=4&AccrualSearch%5Buser%5D=&AccrualSearch%5Bcreated%5D%5B0%5D=&AccrualSearch%5Bcreated%5D%5B1%5D=')

authorize(driver, 'https://bill.bezlimit.ru/site/login', 'loginform-username', 'morozov_i', 'loginform-password', 'Takkurwatak1', '//*[@id="login-form"]/div[4]/div[2]/div[1]/button')

time.sleep(10)

last_hot_activity = get_element_string(driver, '/html/body/div/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[13]')

if calculate_time_difference(time_delta=30, read_time=last_hot_activity) is True:
    message = f"Внимание!\nХот Биллинга НЕТ более 30 минут!\n"

    send_to_telegram(message, '-1001178910709')

driver.quit()
