from billPages.methods.report2Methods import Report2Methods
import pytest


class Test:

    @pytest.mark.smoke
    def test_can_open_page_at_report2(self, browser):
        card = Report2Methods(browser)

        card.go_to_report2_page()

        card.authorization_at_billing()

        card.check_availability()
