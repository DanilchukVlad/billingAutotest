from billPages.locators.report7BlockCodeLocators import Report7BlockCodeLocators
from billPages.baseApp import BasePage


class Report7BlockCodeMethods(Report7BlockCodeLocators, BasePage):

    def go_to_report7_block_code_page(self):
        self.go_to_site(self.report7_block_code_page_url)

    def check_availability(self):
        self.find_element('xpath', self.number_of_records_total)

    def get_number_of_records_total(self):
        item = self.find_element('xpath', self.number_of_records_total)
        return int(str(self.get_value_of_element(item)).replace(' ', ''))
