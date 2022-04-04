from billPages.methods.statisticMethods import StatisticMethods
import pytest


class Test:

    @pytest.mark.smoke
    def test_can_open_statistic_page(self, browser):
        st = StatisticMethods(browser)

        st.go_to_statistic_page()

        st.authorization_at_billing()

        st.check_availability()
