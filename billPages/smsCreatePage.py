from billPages.basePage import BasePage


class SmsCreatePage(BasePage):
    def __init__(self, browser):
        BasePage.__init__(self, browser)

        self.browser = browser

        self.sms_create_page_url = 'https://bill.bezlimit.ru/notify/sms/create'

        self.phone_number_field = "//div[@class='panel-body']/div[1]//input[2]"
        self.text_field = "//div[@class='panel-body']/div[2]//textarea"
        self.calendar_button = "//div[@class='panel-body']/div[3]//span[1]"
        self.reset_date_button = "//div[@class='panel-body']/div[3]//span[2]"
        self.date_field = "//div[@class='panel-body']/div[3]//input"
        self.type_message_button = "//div[@class='panel-body']/div[4]//select"
        self.type_message_list = "//div[@class='panel-body']/div[4]//select/option"
        self.channel_button = "//div[@class='panel-body']/div[5]//select"
        self.channel_list = "//div[@class='panel-body']/div[5]//select/option"

        self.create_button = "//button"

        self.alert_message = "//div[@id='w12-success-0']"

    def go_to_site(self):
        self.browser.get(self.sms_create_page_url)

    def input_phone_number(self, phone: int):
        self.browser.find_element_by_xpath(self.phone_number_field).clear()
        self.browser.find_element_by_xpath(self.phone_number_field).send_keys(phone)

    def input_text(self, text: str):
        self.browser.find_element_by_xpath(self.text_field).clear()
        self.browser.find_element_by_xpath(self.text_field).send_keys(text)

    def input_date(self, date: str):
        self.browser.find_element_by_xpath(self.date_field).clear()
        self.browser.find_element_by_xpath(self.date_field).send_keys(date)

    def click_date_reset_button(self):
        self.browser.find_element_by_xpath(self.reset_date_button).click()

    def click_calendar_button(self):
        self.browser.find_element_by_xpath(self.calendar_button).click()

    def choose_type_message(self, number=1):
        self.browser.find_element_by_xpath(self.type_message_button).click()
        self.browser.find_element_by_xpath(self.type_message_list + f"[{number}]").click()

    def choose_channel(self, number=1):
        self.browser.find_element_by_xpath(self.channel_button).click()
        self.browser.find_element_by_xpath(self.channel_list + f"[{number}]").click()
