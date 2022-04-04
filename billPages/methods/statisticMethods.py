from billPages.locators.statisticLocators import StatisticLocators
from billPages.baseApp import BasePage


class StatisticMethods(StatisticLocators, BasePage):

    def go_to_statistic_page(self):
        self.go_to_site(self.statistic_page_url)

    def check_availability(self):
        self.find_element('xpath', self.section_title)
