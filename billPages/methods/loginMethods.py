from billPages.locators.loginLocators import LoginLocators
from billPages.baseApp import BasePage


class LoginMethods(LoginLocators, BasePage):

    def go_to_login_page(self):
        self.go_to_site(self.login_page_url)

    def go_to_login_page_bill1(self):
        self.go_to_site(self.login_page_bill1_url)

    def check_availability(self):
        self.find_element('id', self.username_textbox_id)

    def check_error(self, message: str):
        error_message = self.find_elements('css_selector', self.error_message_css)
        if message == 'mistake':
            assert self.get_value_of_element(error_message[0]) == 'Incorrect username or password.'
        if message == 'password':
            assert self.get_value_of_element(error_message[0]) == 'Необходимо заполнить «Password».'
        if message == 'username':
            assert self.get_value_of_element(error_message[0]) == 'Необходимо заполнить «Username».'
        if message == 'username&password':
            assert self.get_value_of_element(error_message[0]) == 'Необходимо заполнить «Username».'
            assert self.get_value_of_element(error_message[1]) == 'Необходимо заполнить «Password».'

    def click_login(self):
        button = self.find_element('css_selector', self.login_button_css)
        self.click_on_element(button)

    def enter_username(self, username):
        field = self.find_element('id', self.username_textbox_id)
        self.clear_field(field)
        self.enter_at_field(field, username)

    def enter_password(self, password):
        field = self.find_element('id', self.password_textbox_id)
        self.clear_field(field)
        self.enter_at_field(field, password)
