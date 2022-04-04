from billPages.baseApp import BasePage
from billPages.locators.report17QueueLocators import Report17QueueLocators


class Report17QueueMethods(Report17QueueLocators, BasePage):

    def go_to_report17_queue_page(self):
        self.go_to_site(self.report17_queue_page_url)

    def check_availability(self):
        self.find_element('xpath', self.export_button)

    def choose_in_span_list(self, number=1):
        item = self.find_element('xpath', self.span_list_item+f"[{number}]")

        return self.click_on_element(item)

    def export_to_excel(self):
        button = self.find_element('xpath', self.export_button)
        self.click_on_element(button)

    def get_number_of_records_total(self):
        item = self.find_element('xpath', self.number_of_records_total)

        return int(str(self.get_value_of_element(item)).replace(' ', ''))

    def read_cell(self, line, column):
        cell = self.find_element('xpath', f"//tbody/tr[{line}]/td[{column}]")

        return self.get_value_of_element(cell)

    def reset_filters(self):
        button = self.find_element('xpath', self.reset_filters_button)
        self.click_on_element(button)
