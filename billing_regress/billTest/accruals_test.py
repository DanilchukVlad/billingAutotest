from billPages.methods.accrualsMethods import AccrualsMethods
import pytest


class Test:

    @pytest.mark.smoke
    def test_can_open_page_at_accruals(self, browser):
        accr = AccrualsMethods(browser)

        accr.go_to_accruals_page()

        accr.authorization_at_billing()

        accr.check_availability()

    @pytest.mark.smoke
    def test_check_presence_of_notations_at_accruals(self, browser):
        accr = AccrualsMethods(browser)

        accr.go_to_accruals_page()

        accr.authorization_at_billing()

        accr.check_availability()

        assert accr.get_number_of_records_total() != 0, "В начислениях 0 записей"

    @pytest.mark.smoke
    def test_check_last_hot_at_accruals(self, browser):
        accr = AccrualsMethods(browser)

        accr.go_to_accruals_page()

        accr.authorization_at_billing()

        accr.check_availability()

        accr.filter_by_category("Хот биллинг")

        time = accr.read_cell(1, 13)

        assert accr.calculate_time_difference(30, time) is False, "Последний Хот был больше получаса назад."
