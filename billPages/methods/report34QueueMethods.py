from billPages.baseApp import BasePage
from billPages.locators.report34QueueLocators import Report34QueueLocators


class Report34QueueMethods(Report34QueueLocators, BasePage):

    def go_to_report34_queue_page(self):
        self.go_to_site(self.report34_page_url)

    def check_availability(self):
        self.find_element('xpath', self.create_sms_button)

    def choose_in_span_list(self, number=1):
        item = self.find_element('xpath', self.span_list_item+f"[{number}]")

        return self.click_on_element(item)

    def click_create_sms_button(self):
        button = self.find_element('xpath', self.create_sms_button)
        self.click_on_element(button)

    def filter_by_id(self, identifier: int):
        field = self.find_element("xpath", self.id_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, identifier)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_phone_number(self, phone: int):
        field = self.find_element("xpath", self.phone_number_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, phone)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_company(self, company: str, number=1):
        button = self.find_element('xpath', self.companies_filter_button)
        self.click_on_element(button)

        field = self.find_element('xpath', self.span_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, company)

        self.choose_in_span_list(number)

    def filter_by_text(self, text: str):
        field = self.find_element("xpath", self.text_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, text)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_date_first(self, date: str):
        field = self.find_element("xpath", self.date_sending_first_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, date)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_date_second(self, date: str):
        field = self.find_element("xpath", self.date_sending_second_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, date)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_status_queue(self, number=0):
        button = self.find_element('xpath', self.status_queue_filter_select)
        self.click_on_element(button)

        item = self.find_element('xpath', self.status_queue_filter_select+f"/option[{number}]")
        self.click_on_element(item)

    def filter_by_author(self, author: str, number=1):
        button = self.find_element('xpath', self.author_filter_button)
        self.click_on_element(button)

        field = self.find_element('xpath', self.span_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, author)

        self.choose_in_span_list(number)

    def filter_by_date_addition_first(self, date: str):
        field = self.find_element("xpath", self.date_addition_first_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, date)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_date_addition_second(self, date: str):
        field = self.find_element("xpath", self.date_addition_second_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, date)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_id_smsru(self, idsmsru: str):
        field = self.find_element('xpath', self.id_smsru_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, idsmsru)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_status_smsru(self, number=0):
        button = self.find_element('xpath', self.status_smsru_filter_select)
        self.click_on_element(button)

        item = self.find_element('xpath', self.status_smsru_filter_select+f"/option[{number}]")
        self.click_on_element(item)

    def filter_by_type_message(self, number=0):
        button = self.find_element('xpath', self.type_message_filter_select)
        self.click_on_element(button)

        item = self.find_element('xpath', self.type_message_filter_select+f"/option[{number}]")
        self.click_on_element(item)

    def filter_by_channel(self, number=0):
        button = self.find_element('xpath', self.channel_filter_select)
        self.click_on_element(button)

        item = self.find_element('xpath', self.channel_filter_select+f"/option[{number}]")
        self.click_on_element(item)

    def get_number_of_records_total(self):
        item = self.find_element('xpath', self.number_of_records_total)

        return int(str(self.get_value_of_element(item)).replace(' ', ''))

    def read_cell(self, line, column):
        cell = self.find_element('xpath', f"//tbody/tr[{line}]/td[{column}]")

        return self.get_value_of_element(cell)

    def reset_filters(self):
        button = self.find_element('xpath', self.reset_filters_button)
        self.click_on_element(button)

    def sort_by_id(self):
        button = self.find_element('xpath', self.id_sort_button)
        self.click_on_element(button)

    def sort_by_phone_number(self):
        button = self.find_element('xpath', self.phone_number_sort_button)
        self.click_on_element(button)

    def sort_by_text(self):
        button = self.find_element('xpath', self.text_sort_button)
        self.click_on_element(button)

    def sort_by_date_sending(self):
        button = self.find_element('xpath', self.date_sending_sort_button)
        self.click_on_element(button)

    def sort_by_status(self):
        button = self.find_element('xpath', self.status_queue_sort_button)
        self.click_on_element(button)

    def sort_by_author(self):
        button = self.find_element('xpath', self.author_sort_button)
        self.click_on_element(button)

    def sort_by_date_addition(self):
        button = self.find_element('xpath', self.date_addition_sort_button)
        self.click_on_element(button)

    def sort_by_id_smsru(self):
        button = self.find_element('xpath', self.id_smsru_sort_button)
        self.click_on_element(button)

    def sort_by_status_smsru(self):
        button = self.find_element('xpath', self.status_smsru_sort_button)
        self.click_on_element(button)

    def sort_by_type_message(self):
        button = self.find_element('xpath', self.type_message_sort_button)
        self.click_on_element(button)

    def sort_by_channel(self):
        button = self.find_element('xpath', self.channel_sort_button)
        self.click_on_element(button)
