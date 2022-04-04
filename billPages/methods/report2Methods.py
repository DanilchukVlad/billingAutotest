from billPages.locators.report2Locators import Report2Locators
from billPages.baseApp import BasePage


class Report2Methods(Report2Locators, BasePage):

    def go_to_report2_page(self):
        url = self.report2_page_url
        self.go_to_site(url)

    def check_availability(self):
        self.find_element('xpath', self.ban_filter_select)

    def read_cell(self, line, column):
        cell = self.find_element('xpath', f"//tbody/tr[{line}]/td[{column}]")

        return self.get_value_of_element(cell)
