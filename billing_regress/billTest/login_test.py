from billPages.methods.loginMethods import LoginMethods
import pytest


class Test:

    @pytest.mark.smoke
    def test_login_valid(self, browser):
        login = LoginMethods(browser)

        login.go_to_login_page()

        login.check_availability()

        login.enter_username('butovich_v')
        login.enter_password('Bezlimit2020')
        login.click_login()

    @pytest.mark.regression
    def test_login_with_mistake(self, browser):
        login = LoginMethods(browser)

        login.go_to_login_page()

        login.check_availability()

        login.enter_username('butovich')
        login.enter_password('Bezlimit2020')
        login.click_login()
        login.check_error('mistake')

    @pytest.mark.regression
    def test_login_without_username(self, browser):
        login = LoginMethods(browser)

        login.go_to_login_page()

        login.check_availability()

        login.enter_password('Bezlimit2020')
        login.click_login()
        login.check_error('username')

    @pytest.mark.regression
    def test_login_without_password(self, browser):
        login = LoginMethods(browser)

        login.go_to_login_page()

        login.check_availability()

        login.enter_username('butovich_v')
        login.click_login()
        login.check_error('password')

    @pytest.mark.regression
    def test_login_without_username_and_password(self, browser):
        login = LoginMethods(browser)

        login.go_to_login_page()

        login.check_availability()

        login.click_login()
        login.check_error('username&password')
