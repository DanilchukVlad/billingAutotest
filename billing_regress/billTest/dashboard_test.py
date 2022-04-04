from billPages.methods.dashbordMethods import DashboardMethods
import pytest


class Test:

    @pytest.mark.smoke
    def test_can_open_dashboard_page(self, browser):
        db = DashboardMethods(browser)

        db.go_to_dashboard_page()

        db.authorization_at_billing()

        db.check_availability()
