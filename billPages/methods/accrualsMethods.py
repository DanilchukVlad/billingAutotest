from billPages.locators.accrualsLocators import AccrualsLocators
from billPages.baseApp import BasePage


class AccrualsMethods(AccrualsLocators, BasePage):

    def go_to_accruals_page(self):
        self.go_to_site(self.accruals_page_url)

    def check_availability(self):
        self.find_element('xpath', self.export_button)

    def choose_in_span_list(self, number):
        item = self.find_element('xpath', self.span_list_item+f"[{number}]")

        return self.click_on_element(item)

    def export_to_excel(self):
        button = self.find_element('xpath', self.export_button)
        self.click_on_element(button)

    def get_number_of_records_total(self):
        item = self.find_element('xpath', self.number_of_records_total)

        return int(str(self.get_value_of_element(item)).replace(' ', ''))

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

    def sort_by_consumption(self):
        button = self.find_element('xpath', self.consumption_sort_button)
        self.click_on_element(button)

    def sort_by_date_beginning(self):
        button = self.find_element('xpath', self.date_beginning_sort_button)
        self.click_on_element(button)

    def sort_by_date_end(self):
        button = self.find_element('xpath', self.date_end_sort_button)
        self.click_on_element(button)

    def sort_by_feature_code(self):
        button = self.find_element('xpath', self.feature_code_sort_button)
        self.click_on_element(button)

    def sort_by_comment(self):
        button = self.find_element('xpath', self.comment_sort_button)
        self.click_on_element(button)

    def sort_by_category(self):
        button = self.find_element('xpath', self.category_sort_button)
        self.click_on_element(button)

    def sort_by_user(self):
        button = self.find_element('xpath', self.user_sort_button)
        self.click_on_element(button)

    def sort_by_date_created(self):
        button = self.find_element('xpath', self.date_created_sort_button)
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

    def filter_by_tariff_now(self, tariff: str, number=1):
        button = self.find_element('xpath', self.tariff_now_filter_button)
        self.click_on_element(button)

        field = self.find_element('xpath', self.span_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, tariff)

        self.choose_in_span_list(number)

    def filter_by_companies(self, company: str, number=1):
        button = self.find_element('xpath', self.companies_filter_button)
        self.click_on_element(button)

        field = self.find_element('xpath', self.span_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, company)

        self.choose_in_span_list(number)

    def filter_by_category(self, category: str, number=1):
        button = self.find_element('xpath', self.category_filter_button)
        self.click_on_element(button)

        field = self.find_element('xpath', self.span_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, category)

        self.choose_in_span_list(number)

    def read_cell(self, line, column):
        cell = self.find_element('xpath', f"//tbody/tr[{line}]/td[{column}]")

        return self.get_value_of_element(cell)
