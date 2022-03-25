from billing.billing_function import authorize
from selenium import webdriver
import time
from telegram_pack.send_telegram import send_to_telegram
from billing.methods.report2_methods import get_element
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/butovich_v/workspace/billingautotest/driver/chromedriver_lnx')

time.sleep(5)

authorize(driver, 'https://bill.bezlimit.ru/site/login', 'loginform-username', 'morozov_i', 'loginform-password', 'Takkurwatak1', '//*[@id="login-form"]/div[4]/div[2]/div[1]/button')

time.sleep(5)

driver.get('https://bill.bezlimit.ru/report/monitoring')

time.sleep(5)

max_active_time = get_element(driver, '/html/body/div[1]/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[38]').split('[')[1]
max_active_time = max_active_time.split(']')[0]

if max_active_time[0:4] != "17:0":
    message = f"Внимание! Вероятность ошибки переблокировки\n" \
              f"Последнее время максимальной активности - {max_active_time}"

    send_to_telegram(message, '-1001179024349')

driver.quit()
