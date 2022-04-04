from billPages.locators.report7StatusLocators import Report7StatusLocators
from billPages.baseApp import BasePage


class Report7StatusMethods(Report7StatusLocators, BasePage):

    def go_to_report7_status_page(self):
        self.go_to_site(self.report7_status_page_url)

    def check_availability(self):
        self.find_element('xpath', self.number_of_records_total)

    def get_number_of_records_total(self):
        item = self.find_element('xpath', self.number_of_records_total)
        return int(str(self.get_value_of_element(item)).replace(' ', ''))
