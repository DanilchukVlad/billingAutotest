from billPages.locators.report1Locators import Report1Locators
from billPages.baseApp import BasePage


class Report1Methods(Report1Locators, BasePage):

    def go_to_report1_page(self):
        url = self.report1_page_url
        self.go_to_site(url)

    def check_availability(self):
        self.find_element('xpath', self.number_of_records_total)

    def choose_in_span_list(self, number):
        item = self.find_element('xpath', self.span_list_item+f"[{number}]")

        return self.click_on_element(item)

    # filters

    def filter_by_task_source(self, source: str):
        field = self.find_element('xpath', self.task_source_filter_field)
        self.clear_field(field)
        self.enter_at_field(field, source)
        self.press_a_button_on_a_keyboard(field, 'Enter')

    # filters

    def filter_by_queue_status(self, number=0):
        button = self.find_element('xpath', self.queue_status_filter_select)
        self.click_on_element(button)

        item = self.find_element('xpath', self.queue_status_filter_select+f"/option[{number}]")
        self.click_on_element(item)

    def read_cell(self, line, column):
        cell = self.find_element('xpath', f"//tbody/tr[{line}]/td[{column}]")

        return self.get_value_of_element(cell)

    def reset_filters(self):
        button = self.find_element('xpath', self.reset_filters_button)
        self.click_on_element(button)
