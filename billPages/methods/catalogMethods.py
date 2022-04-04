from billPages.baseApp import BasePage
from billPages.locators.catalogLocators import CatalogLocators


class CatalogMethods(CatalogLocators, BasePage):

    def go_to_catalog_page(self):
        self.go_to_site(self.catalog_page_url)

    def go_to_catalog_page_bill1(self):
        self.go_to_site(self.catalog_page_bill1_url)

    def check_availability(self):
        self.find_element('xpath', self.reset_filters_button)

    def choose_in_span_list(self, number):
        item = self.find_element('xpath', self.span_list_item+f"[{number}]")

        return self.click_on_element(item)

    def copy_chosen_numbers(self):
        button = self.find_element('xpath', self.copy_button)
        self.click_on_element(button)

    def export(self):
        button = self.find_element('xpath', self.export_button)
        self.click_on_element(button)

    def export_pd(self):
        button = self.find_element('xpath', self.export_pd_button)
        self.click_on_element(button)

    def filter_by_phone_number(self, phone: str):
        field = self.find_element("xpath", self.phone_number_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, phone)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_status(self, number=0):
        button = self.find_element('xpath', self.status_filter_select)
        self.click_on_element(button)

        item = self.find_element('xpath', self.status_filter_select+f"/option[{number}]")
        self.click_on_element(item)

    def filter_by_date_activation_first(self, date: str):
        field = self.find_element("xpath", self.date_activation_first_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, date)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_date_activation_second(self, date: str):
        field = self.find_element("xpath", self.date_activation_second_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, date)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_date_blocking_first(self, date: str):
        field = self.find_element("xpath", self.date_blocking_first_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, date)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_date_blocking_second(self, date: str):
        field = self.find_element("xpath", self.date_blocking_second_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, date)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_expiration_date_first(self, date: str):
        field = self.find_element("xpath", self.expiration_date_first_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, date)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_expiration_date_second(self, date: str):
        field = self.find_element("xpath", self.expiration_date_second_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, date)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_balance(self, balance: str):
        field = self.find_element('xpath', self.balance_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, balance)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_balance_without_fluidity(self, balance: str):
        field = self.find_element('xpath', self.balance_without_fluidity_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, balance)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_current_accrual(self, accrual: str):
        field = self.find_element('xpath', self.current_accrual_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, accrual)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_balance_plus_score(self, balance: str):
        field = self.find_element('xpath', self.balance_plus_score_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, balance)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_contact_person(self, person: str, number=1):
        button = self.find_element('xpath', self.contact_person_filter_button)
        self.click_on_element(button)

        field = self.find_element('xpath', self.span_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, person)

        self.choose_in_span_list(number)

    def filter_by_company(self, company: str, number=1):
        field = self.find_element('xpath', self.span_ban_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, company)

        self.choose_in_span_list(number)

    def filter_by_blocking_prohibition(self, number=0):
        button = self.find_element('xpath', self.blocking_prohibition_filter_select)
        self.click_on_element(button)

        item = self.find_element('xpath', self.blocking_prohibition_filter_select+f"/option[{number}]")
        self.click_on_element(item)

    def filter_by_comment_blocking_prohibition(self, comment: str):
        field = self.find_element('xpath', self.comment_blocking_prohibition_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, comment)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_unblocking_prohibition(self, number=0):
        button = self.find_element('xpath', self.unblocking_prohibition_filter_select)
        self.click_on_element(button)

        item = self.find_element('xpath', self.unblocking_prohibition_filter_select+f"/option[{number}]")
        self.click_on_element(item)

    def filter_by_comment_unblocking_prohibition(self, comment: str):
        field = self.find_element('xpath', self.comment_unblocking_prohibition_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, comment)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_international_roaming(self, number=0):
        button = self.find_element('xpath', self.international_roaming_filter_select)
        self.click_on_element(button)

        item = self.find_element('xpath', self.international_roaming_filter_select+f"/option[{number}]")
        self.click_on_element(item)

    def filter_by_id_dealer(self, identifier: str):
        field = self.find_element('xpath', self.id_dealer_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, identifier)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_dealer_branch(self, dealer: str, number=1):
        button = self.find_element('xpath', self.dealer_branch_filter_button)
        self.click_on_element(button)

        field = self.find_element('xpath', self.span_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, dealer)

        self.choose_in_span_list(number)

    def filter_by_template(self, template: str):
        field = self.find_element('xpath', self.template_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, template)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_category(self, number=0):
        button = self.find_element('xpath', self.category_filter_select)
        self.click_on_element(button)

        item = self.find_element('xpath', self.category_filter_select+f"/option[{number}]")
        self.click_on_element(item)

    def filter_by_main_digit_number(self, digit: str):
        field = self.find_element('xpath', self.main_digit_number_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, digit)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def filter_by_minimum_tariff_limitation(self, limit: str):
        field = self.find_element('xpath', self.minimum_tariff_limitation_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, limit)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    def go_to_exports_result(self):
        button = self.find_element('xpath', self.results_export_button)
        self.click_on_element(button)

    def go_to_group_search_modal_window(self):
        button = self.find_element('xpath', self.group_search_button)
        self.click_on_element(button)

    def go_to_group_operations(self):
        button = self.find_element('xpath', self.group_operation_button)
        self.click_on_element(button)

    def go_to_group_mailing(self):
        button = self.find_element('xpath', self.sms_distribution_button)
        self.click_on_element(button)

    def go_to_columns_modal_window(self):
        button = self.find_element('xpath', self.columns_button)
        self.click_on_element(button)

    def get_number_of_records_total(self):
        item = self.find_element('xpath', self.number_of_records_total)

        return int(str(self.get_value_of_element(item)).replace(' ', ''))

    def read_cell(self, line, column):
        cell = self.find_element('xpath', f"//tbody/tr[{line}]/td[{column}]")

        return self.get_value_of_element(cell)

    def read_filter_err_message(self, column):
        msg = self.find_element('xpath', self.filter_err_message + f'[{column}]')

        return self.get_value_of_element(msg)

    def reset_filters(self):
        button = self.find_element('xpath', self.reset_filters_button)
        self.click_on_element(button)

    def select_all(self):
        button = self.find_element('xpath', self.total_checkbox)
        self.click_on_element(button)

    def sort_by_phone_number(self):
        button = self.find_element('xpath', self.phone_number_sort_button)
        self.click_on_element(button)

    def sort_by_status(self):
        button = self.find_element('xpath', self.status_sort_button)
        self.click_on_element(button)

    def sort_by_date_activation(self):
        button = self.find_element('xpath', self.date_activation_sort_button)
        self.click_on_element(button)

    def sort_by_date_blocking(self):
        button = self.find_element('xpath', self.date_blocking_sort_button)
        self.click_on_element(button)

    def sort_by_expiration_date(self):
        button = self.find_element('xpath', self.expiration_date_sort_button)
        self.click_on_element(button)

    def sort_by_balance(self):
        button = self.find_element('xpath', self.balance_sort_button)
        self.click_on_element(button)

    def sort_by_current_accrual(self):
        button = self.find_element('xpath', self.current_accrual_sort_button)
        self.click_on_element(button)

    def sort_by_balance_plus_score(self):
        button = self.find_element('xpath', self.balance_plus_score_sort_button)
        self.click_on_element(button)

    def sort_by_contact_person(self):
        button = self.find_element('xpath', self.contact_person_sort_button)
        self.click_on_element(button)

    def sort_by_blocking_prohibition(self):
        button = self.find_element('xpath', self.blocking_prohibition_sort_button)
        self.click_on_element(button)

    def sort_by_comment_blocking_prohibition(self):
        button = self.find_element('xpath', self.comment_blocking_prohibition_sort_button)
        self.click_on_element(button)

    def sort_by_unblocking_prohibition(self):
        button = self.find_element('xpath', self.unblocking_prohibition_sort_button)
        self.click_on_element(button)

    def sort_by_comment_unblocking_prohibition(self):
        button = self.find_element('xpath', self.comment_unblocking_prohibition_sort_button)
        self.click_on_element(button)

    def sort_by_id_dealer(self):
        button = self.find_element('xpath', self.id_dealer_sort_button)
        self.click_on_element(button)

    def sort_by_category(self):
        button = self.find_element('xpath', self.category_sort_button)
        self.click_on_element(button)

    def sort_by_main_digit_number(self):
        button = self.find_element('xpath', self.main_digit_number_sort_button)
        self.click_on_element(button)

    def sort_by_code(self):
        button = self.find_element('xpath', self.code_sort_button)
        self.click_on_element(button)

    def sort_by_mask(self):
        button = self.find_element('xpath', self.mask_sort_button)
        self.click_on_element(button)

    def sort_by_reservation(self):
        button = self.find_element('xpath', self.reservation_sort_button)
        self.click_on_element(button)

    def sort_by_arpu(self):
        button = self.find_element('xpath', self.arpu_sort_button)
        self.click_on_element(button)

    def sort_by_package(self):
        button = self.find_element('xpath', self.package_sort_button)
        self.click_on_element(button)

    def sort_by_secret_word(self):
        button = self.find_element('xpath', self.secret_word_sort_button)
        self.click_on_element(button)

    def sort_by_camel(self):
        button = self.find_element('xpath', self.camel_sort_button)
        self.click_on_element(button)

    def sort_by_financial_status(self):
        button = self.find_element('xpath', self.financial_status_sort_button)
        self.click_on_element(button)

    def sort_by_payment(self):
        button = self.find_element('xpath', self.payment_sort_button)
        self.click_on_element(button)

    def sort_by_unprofitable_subscriber(self):
        button = self.find_element('xpath', self.unprofitable_subscriber_sort_button)
        self.click_on_element(button)

    def sort_by_prohibition_false_tariff(self):
        button = self.find_element('xpath', self.prohibition_false_tariff_sort_button)
        self.click_on_element(button)

    def sort_by_frod_dangerous(self):
        button = self.find_element('xpath', self.frod_dangerous_blocking_prohibition_sort_button)
        self.click_on_element(button)

    def sort_by_sign_number_store(self):
        button = self.find_element('xpath', self.sign_number_store_sort_button)
        self.click_on_element(button)

    def sort_by_sign_number(self):
        button = self.find_element('xpath', self.sign_number_sort_button)
        self.click_on_element(button)

    def sort_by_main_group_number(self):
        button = self.find_element('xpath', self.main_group_number_sort_button)
        self.click_on_element(button)

    def sort_by_free_output(self):
        button = self.find_element('xpath', self.free_output_sort_button)
        self.click_on_element(button)
