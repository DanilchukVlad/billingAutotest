class AccrualsLocators:

    accruals_page_url = 'https://bill.bezlimit.ru/finance/accrual'

    reset_filters_button = "//a[@class='btn btn-sm btn-purple btn-icon fal fa-filter']"
    export_button = "//a[@class='btn btn-success btn-sm btn-labeled fa fa-table']"

    number_of_records_total = "//div[@id='w0']/div/b[2]"

    id_sort_button = "//a[@data-sort='id']"
    phone_number_sort_button = "//a[@data-sort='phone_number']"
    companies_sort_button = "//a[@data-sort='account_id']"
    consumption_sort_button = "//a[@data-sort='amount']"
    date_beginning_sort_button = "//a[@data-sort='date']"
    date_end_sort_button = "//a[@data-sort='date_end']"
    feature_code_sort_button = "//a[@data-sort='feature_id']"
    comment_sort_button = "//a[@data-sort='description']"
    category_sort_button = "//a[@data-sort='minus_category_id']"
    user_sort_button = "//a[@data-sort='user']"
    date_created_sort_button = "//a[@data-sort='created']"

    id_filter_field = "//tr[@id='w0-filters']/td[1]/input"
    phone_number_filter_field = "//tr[@id='w0-filters']/td[2]/input"
    tariff_now_filter_button = "//tr[@id='w0-filters']/td[3]/span"
    companies_filter_button = "//tr[@id='w0-filters']/td[4]/span"
    consumption_filter_field = "//tr[@id='w0-filters']/td[6]/input"
    date_beginning_first_filter_field = "//tr[@id='w0-filters']/td[7]/input[1]"
    date_beginning_second_filter_field = "//tr[@id='w0-filters']/td[7]/input[2]"
    date_end_first_filter_field = "//tr[@id='w0-filters']/td[8]/input[1]"
    date_end_second_filter_field = "//tr[@id='w0-filters']/td[8]/input[2]"
    feature_code_filter_button = "//tr[@id='w0-filters']/td[9]/span"
    comment_filter_field = "//tr[@id='w0-filters']/td[10]/input"
    category_filter_button = "//tr[@id='w0-filters']/td[11]/span"
    date_created_first_filter_field = "//tr[@id='w0-filters']/td[13]/input[1]"
    date_created_second_filter_field = "//tr[@id='w0-filters']/td[13]/input[2]"

    span_filter_field = "//input[@type='search']"
    span_list_item = "//span[@class='select2-results']/ul/li"
