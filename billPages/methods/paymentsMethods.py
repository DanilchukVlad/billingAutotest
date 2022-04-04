from billPages.baseApp import BasePage
from billPages.locators.paymentsLocators import PaymentsLocators


class PaymentsMethods(PaymentsLocators, BasePage):

    def go_to_payments_page(self):
        self.go_to_site(self.payments_page_url)

    def check_availability(self):
        self.find_element('xpath', self.export_button)

    def choose_in_span_list(self, number=1):
        item = self.find_element('xpath', self.span_list_item+f"[{number}]")

        return self.click_on_element(item)

    def export_to_excel(self):
        button = self.find_element('xpath', self.export_button)
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

    def filter_by_sum(self, value: str):
        field = self.find_element("xpath", self.sum_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, value)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_date_first(self, date: str):
        field = self.find_element("xpath", self.date_first_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, date)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_date_second(self, date: str):
        field = self.find_element("xpath", self.date_second_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, date)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_comment(self, comment: str):
        field = self.find_element("xpath", self.comment_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, comment)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_category(self, category: str, number=1):
        button = self.find_element('xpath', self.category_filter_button)
        self.click_on_element(button)

        field = self.find_element('xpath', self.span_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, category)

        self.choose_in_span_list(number)

    def filter_by_created_first(self, date: str):
        field = self.find_element("xpath", self.created_first_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, date)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_created_second(self, date: str):
        field = self.find_element("xpath", self.created_second_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, date)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_user(self, user: str, number=1):
        button = self.find_element('xpath', self.user_filter_button)
        self.click_on_element(button)

        field = self.find_element('xpath', self.span_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, user)

        self.choose_in_span_list(number)

    def filter_by_payment_type(self, number=0):
        button = self.find_element('xpath', self.payment_type_filter_select)
        self.click_on_element(button)

        item = self.find_element('xpath', self.payment_type_filter_select+f"/option[{number}]")
        self.click_on_element(item)

    def filter_by_payment_system(self, number=0):
        button = self.find_element('xpath', self.payment_system_filter_select)
        self.click_on_element(button)

        item = self.find_element('xpath', self.payment_system_filter_select+f"/option[{number}]")
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

    def sort_by_companies(self):
        button = self.find_element('xpath', self.companies_sort_button)
        self.click_on_element(button)

    def sort_by_date(self):
        button = self.find_element('xpath', self.date_sort_button)
        self.click_on_element(button)

    def sort_by_comment(self):
        button = self.find_element('xpath', self.comment_sort_button)
        self.click_on_element(button)

    def sort_by_category(self):
        button = self.find_element('xpath', self.category_sort_button)
        self.click_on_element(button)

    def sort_by_created(self):
        button = self.find_element('xpath', self.created_sort_button)
        self.click_on_element(button)

    def sort_by_user(self):
        button = self.find_element('xpath', self.user_sort_button)
        self.click_on_element(button)

    def sort_by_payment_type(self):
        button = self.find_element('xpath', self.payment_type_sort_button)
        self.click_on_element(button)

    def sort_by_payment_system(self):
        button = self.find_element('xpath', self.payment_system_sort_button)
        self.click_on_element(button)
