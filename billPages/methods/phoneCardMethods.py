from billPages.locators.phoneCardLocators import PhoneCardLocators
from billPages.baseApp import BasePage


class PhoneCardMethods(PhoneCardLocators, BasePage):

    def go_to_phone_card_page(self, number: int):
        url = self.phone_card_page_url + str(number)
        self.go_to_site(url)

    def check_availability(self):
        self.find_element('xpath', self.pd_block)
