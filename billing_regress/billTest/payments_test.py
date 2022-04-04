from billPages.methods.paymentsMethods import PaymentsMethods
import pytest


class Test:

    @pytest.mark.smoke
    def test_can_open_page_at_payments(self, browser):
        pay = PaymentsMethods(browser)

        pay.go_to_payments_page()

        pay.authorization_at_billing()

        pay.check_availability()

    @pytest.mark.smoke
    def test_check_presence_of_notations_at_payments(self, browser):
        pay = PaymentsMethods(browser)

        pay.go_to_payments_page()

        pay.authorization_at_billing()

        pay.check_availability()

        assert pay.get_number_of_records_total() != 0, "В начислениях 0 записей"

    @pytest.mark.smoke
    def test_check_last_sber_and_bee_payments_at_payments(self, browser):
        pay = PaymentsMethods(browser)

        pay.go_to_payments_page()

        pay.authorization_at_billing()

        pay.check_availability()

        pay.filter_by_category("[5] Наличный платеж (Билайн)")
        assert pay.calculate_time_difference(time_delta=30, read_time=pay.read_cell(1, 8)) is False, \
            "Последний платеж [5] был больше получаса назад."

        pay.filter_by_category("[10] Платеж Sberbank online")
        assert pay.calculate_time_difference(time_delta=30, read_time=pay.read_cell(1, 8)) is False, \
            "Последний платеж [10] был больше получаса назад."
