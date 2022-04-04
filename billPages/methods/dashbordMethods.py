from billPages.locators.dashboardLocators import DashboardLocators
from billPages.baseApp import BasePage


class DashboardMethods(DashboardLocators, BasePage):

    def go_to_dashboard_page(self):
        self.go_to_site(self.dashboard_page_url)

    def check_availability(self):
        self.find_element('xpath', self.statistic_bloc)
