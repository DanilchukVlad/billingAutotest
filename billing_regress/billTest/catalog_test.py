from billPages.methods.catalogMethods import CatalogMethods
import pytest
import time


class Test:

    @pytest.mark.smoke
    def test_can_open_page_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

    @pytest.mark.smoke
    def test_check_presence_of_notations_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        assert cat.get_number_of_records_total() > 700000, "В каталоге меньше 700к записей"

    @pytest.mark.regression
    def test_check_phone_number_filter_with_one_valid_number_at_catalog(self, browser):
        cat = CatalogMethods(browser)
        phone_number = '9696588825'

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        cat.filter_by_phone_number(phone_number)

        cat.check_availability()

        assert cat.read_cell(column=2, line=1) == phone_number

    @pytest.mark.regression
    def test_check_phone_number_filter_with_one_invalid_number_at_catalog(self, browser):
        cat = CatalogMethods(browser)
        phone_number = '9999999999'

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        cat.filter_by_phone_number(phone_number)

        cat.check_availability()

        assert cat.read_cell(column=1, line=1) == 'Ничего не найдено.'

    @pytest.mark.regression
    def test_check_phone_number_filter_with_piece_of_number_at_catalog(self, browser):
        cat = CatalogMethods(browser)
        phone_number = '7777777'

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        cat.filter_by_phone_number(phone_number)

        cat.check_availability()

        for i in range(1, cat.get_number_of_records_total()):
            assert '7777777' in cat.read_cell(column=2, line=i)

    @pytest.mark.regression
    def test_check_phone_number_filter_with_not_numeric_number_at_catalog(self, browser):
        cat = CatalogMethods(browser)
        phone_number = 'q'

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        cat.filter_by_phone_number(phone_number)

        cat.check_availability()

        assert cat.read_cell(column=1, line=1) == 'Ничего не найдено.'
        assert cat.read_filter_err_message(column=2) == 'Значение «Номер» должно быть целым числом.'

    @pytest.mark.regression
    def test_check_status_filter_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        count_all = cat.get_number_of_records_total()

        cat.filter_by_status(number=2)

        cat.check_availability()

        count_active = cat.get_number_of_records_total()

        cat.filter_by_status(number=3)

        cat.check_availability()

        count_block = cat.get_number_of_records_total()

        assert count_all == count_active + count_block

    @pytest.mark.regression
    def test_check_date_activation_filter_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        count_all = cat.get_number_of_records_total()
        date = cat.read_cell(column=4, line=1)

        cat.filter_by_date_activation_first(date)

        cat.check_availability()

        count_after = cat.get_number_of_records_total()

        cat.reset_filters()

        cat.check_availability()

        assert count_all == cat.get_number_of_records_total()

        cat.filter_by_date_activation_second(date)

        cat.check_availability()

        count_before = cat.get_number_of_records_total()

        cat.filter_by_date_activation_first(date)

        cat.check_availability()

        count_between = cat.get_number_of_records_total()

        assert (count_after + count_before) - count_all == count_between

    @pytest.mark.regression
    def test_check_date_blocking_filter_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        count_all = cat.get_number_of_records_total()
        date = cat.read_cell(column=5, line=1)

        cat.filter_by_date_blocking_first(date)

        cat.check_availability()

        count_after = cat.get_number_of_records_total()

        cat.reset_filters()

        cat.check_availability()

        assert count_all == cat.get_number_of_records_total()

        cat.filter_by_date_blocking_second(date)

        cat.check_availability()

        count_before = cat.get_number_of_records_total()

        cat.filter_by_date_blocking_first(date)

        cat.check_availability()

        count_between = cat.get_number_of_records_total()

        assert (count_after + count_before) - count_all == count_between

    @pytest.mark.regression
    @pytest.mark.xfail
    def test_check_expiration_date_filter_at_catalog(self, browser):
        from datetime import datetime

        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        count_all = cat.get_number_of_records_total()

        today = datetime.today()
        first_day = datetime(today.year, today.month, 1).strftime('%Y-%m-%d')

        cat.filter_by_expiration_date_first(first_day)

        cat.check_availability()

        first_res = cat.get_number_of_records_total()

        cat.reset_filters()

        cat.check_availability()

        cat.filter_by_expiration_date_second(first_day)

        cat.check_availability()

        second_res = cat.get_number_of_records_total()

        assert second_res + first_res == count_all

    @pytest.mark.regression
    def test_check_balance_filter_with_one_valid_value_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        balance = cat.read_cell(column=7, line=1)

        cat.filter_by_balance(balance=balance)

        cat.check_availability()

        count_all = cat.get_number_of_records_total()

        for i in range(1, count_all if count_all < 200 else 200):
            assert cat.read_cell(column=7, line=i) == balance

    @pytest.mark.regression
    def test_check_balance_filter_with_one_invalid_value_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        balance = 'dfgsf'

        cat.filter_by_balance(balance=balance)

        cat.check_availability()

        assert cat.read_filter_err_message(column=7) == "Значение «Баланс» неверно."

    @pytest.mark.regression
    def test_check_balance_without_fluidity_filter_with_one_valid_value_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        balance = cat.read_cell(column=8, line=1)

        cat.filter_by_balance_without_fluidity(balance=balance)

        cat.check_availability()

        count_all = cat.get_number_of_records_total()

        for i in range(1, count_all if count_all < 200 else 200):
            assert cat.read_cell(column=8, line=i) == balance

    @pytest.mark.regression
    def test_check_balance_without_fluidity_filter_with_one_invalid_value_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        balance = 'dfgsf'

        cat.filter_by_balance_without_fluidity(balance=balance)

        cat.check_availability()

        assert cat.read_filter_err_message(column=8) == "Значение «Баланс без текучки» неверно."

    @pytest.mark.regression
    def test_check_current_accrual_filter_with_one_valid_value_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        accrual = cat.read_cell(column=9, line=1)

        cat.filter_by_current_accrual(accrual=accrual)

        cat.check_availability()

        count_all = cat.get_number_of_records_total()

        for i in range(1, count_all if count_all < 200 else 200):
            assert cat.read_cell(column=9, line=i) == accrual

    @pytest.mark.regression
    def test_check_current_accrual_filter_with_one_invalid_value_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        accrual = 'dfgsf'

        cat.filter_by_current_accrual(accrual=accrual)

        cat.check_availability()

        assert cat.read_filter_err_message(column=9) == "Значение «Текущее начисление» неверно."

    @pytest.mark.regression
    def test_check_balance_plus_score_filter_with_one_valid_value_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        balance = cat.read_cell(column=10, line=1)

        cat.filter_by_balance_plus_score(balance=balance)

        cat.check_availability()

        count_all = cat.get_number_of_records_total()

        for i in range(1, count_all if count_all < 200 else 200):
            assert cat.read_cell(column=10, line=i) == balance

    @pytest.mark.regression
    def test_check_balance_plus_score_filter_with_one_invalid_value_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        balance = 'dfgsf'

        cat.filter_by_balance_plus_score(balance=balance)

        cat.check_availability()

        assert cat.read_filter_err_message(column=10) == "Значение «Баланс + счет» неверно."

    @pytest.mark.regression
    def test_check_contact_person_filter_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        person = cat.read_cell(column=11, line=1)

        cat.filter_by_contact_person(person=person)

        cat.check_availability()

        count_all = cat.get_number_of_records_total()

        for i in range(1, count_all if count_all < 200 else 200):
            assert person in cat.read_cell(column=11, line=i)

    @pytest.mark.regression
    def test_check_company_filter_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        company = cat.read_cell(column=12, line=1)

        cat.filter_by_company(company=company)

        cat.check_availability()

        count_all = cat.get_number_of_records_total()

        for i in range(1, count_all if count_all < 200 else 200):
            assert company in cat.read_cell(column=12, line=i)

    @pytest.mark.regression
    def test_check_blocking_prohibition_filter_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        count_all = cat.get_number_of_records_total()

        cat.filter_by_blocking_prohibition(number=2)

        cat.check_availability()

        count_yes = cat.get_number_of_records_total()

        cat.filter_by_blocking_prohibition(number=3)

        cat.check_availability()

        count_no = cat.get_number_of_records_total()

        assert count_all == count_yes + count_no

    @pytest.mark.regression
    def test_check_comment_blocking_prohibition_filter_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        cat.sort_by_comment_blocking_prohibition()

        cat.check_availability()

        cat.sort_by_comment_blocking_prohibition()

        cat.check_availability()

        comment = cat.read_cell(column=15, line=1)

        cat.filter_by_comment_blocking_prohibition(comment=comment)

        cat.check_availability()

        count_all = cat.get_number_of_records_total()

        for i in range(1, count_all if count_all < 200 else 200):
            assert comment in cat.read_cell(column=15, line=i)

    @pytest.mark.regression
    def test_check_unblocking_prohibition_filter_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        count_all = cat.get_number_of_records_total()

        cat.filter_by_unblocking_prohibition(number=2)

        cat.check_availability()

        count_yes = cat.get_number_of_records_total()

        cat.filter_by_unblocking_prohibition(number=3)

        cat.check_availability()

        count_no = cat.get_number_of_records_total()

        assert count_all == count_yes + count_no

    @pytest.mark.regression
    def test_check_comment_unblocking_prohibition_filter_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        cat.sort_by_comment_unblocking_prohibition()

        cat.check_availability()

        cat.sort_by_comment_unblocking_prohibition()

        cat.check_availability()

        comment = cat.read_cell(column=17, line=1)

        cat.filter_by_comment_unblocking_prohibition(comment=comment)

        cat.check_availability()

        count_all = cat.get_number_of_records_total()

        for i in range(1, count_all if count_all < 200 else 200):
            assert comment in cat.read_cell(column=17, line=i)

    @pytest.mark.regression
    def test_check_international_roaming_filter_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        count_all = cat.get_number_of_records_total()

        cat.filter_by_international_roaming(number=2)

        cat.check_availability()

        count_yes = cat.get_number_of_records_total()

        cat.filter_by_international_roaming(number=3)

        cat.check_availability()

        count_no = cat.get_number_of_records_total()

        assert count_all == count_yes + count_no

    @pytest.mark.regression
    def test_check_id_dealer_filter_with_one_valid_id_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        identifier = cat.read_cell(column=19, line=1).split(' ')[0][1:-1]

        cat.filter_by_id_dealer(identifier)

        cat.check_availability()

        count_all = cat.get_number_of_records_total()

        for i in range(1, count_all if count_all < 200 else 200):
            assert identifier in cat.read_cell(column=19, line=i)

    @pytest.mark.regression
    def test_check_id_dealer_filter_with_one_invalid_str_id_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        identifier = "sklgsp"

        cat.filter_by_id_dealer(identifier)

        cat.check_availability()

        assert cat.read_filter_err_message(column=19) == "Значение «Дилер» должно быть целым числом."

    @pytest.mark.xfail
    @pytest.mark.regression
    def test_check_dealer_branch_filter_with_valid_value_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        dealer = cat.read_cell(column=20, line=1)

        cat.filter_by_dealer_branch(dealer)

        time.sleep(5)

        cat.check_availability()

        count_all = cat.get_number_of_records_total()

        for i in range(1, count_all if count_all < 200 else 200):
            assert dealer in cat.read_cell(column=20, line=i)

    @pytest.mark.regression
    def test_check_template_filter_with_one_valid_value_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        template = cat.read_cell(column=21, line=1)

        cat.filter_by_template(template)

        cat.check_availability()

        count_all = cat.get_number_of_records_total()

        for i in range(1, count_all if count_all < 200 else 200):
            assert template in cat.read_cell(column=21, line=i)

    @pytest.mark.regression
    def test_check_category_filter_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        cat.filter_by_category(number=3)

        count_all = cat.get_number_of_records_total()

        cat.check_availability()

        for i in range(1, count_all if count_all < 200 else 200):
            assert "brilliant_super" == cat.read_cell(column=22, line=i)

    @pytest.mark.regression
    def test_check_main_digit_number_filter_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        digit = cat.read_cell(column=23, line=1)

        cat.filter_by_main_digit_number(digit=digit)

        count_all = cat.get_number_of_records_total()

        cat.check_availability()

        for i in range(1, count_all if count_all < 200 else 200):
            assert digit in cat.read_cell(column=23, line=i)

    @pytest.mark.xfail
    @pytest.mark.regression
    def test_check_minimum_tariff_limitation_filter_at_catalog(self, browser):
        cat = CatalogMethods(browser)

        cat.go_to_catalog_page()

        cat.authorization_at_billing()

        cat.check_availability()

        limit = cat.read_cell(column=24, line=1)

        cat.filter_by_minimum_tariff_limitation(limit=limit)

        cat.check_availability()

        count_all = cat.get_number_of_records_total()

        for i in range(1, count_all if count_all < 200 else 200):
            assert limit == cat.read_cell(column=24, line=i)
