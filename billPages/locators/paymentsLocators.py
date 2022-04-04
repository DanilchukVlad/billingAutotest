class PaymentsLocators:

    payments_page_url = 'https://bill.bezlimit.ru/finance/plus'

    reset_filters_button = "//a[@class='btn btn-sm btn-purple btn-icon fal fa-filter']"
    payment_card_button = "//button[@class='btn btn-dark btn-labeled fal fa-credit-card']"
    export_button = "//a[@class='btn btn-success btn-labeled fal fa-table']"
    accept_payment_button = "//a[@class='btn btn-primary btn-labeled fal fa-plus']"
    payment_categories_button = "//a[@class='btn btn-info btn-labeled fal fa-list']"

    promotion_bbms_button = "//ul[@id='w2']/li[2]/a"

    number_of_records_total = "//div[@id='w0']/div/b[2]"

    id_sort_button = "//thead/tr[1]/th[1]/a"
    phone_number_sort_button = "//thead/tr[1]/th[2]/a"
    companies_sort_button = "//thead/tr[1]/th[3]/a"
    date_sort_button = "//thead/tr[1]/th[5]/a"
    comment_sort_button = "//thead/tr[1]/th[6]/a"
    category_sort_button = "//thead/tr[1]/th[7]/a"
    created_sort_button = "//thead/tr[1]/th[8]/a"
    user_sort_button = "//thead/tr[1]/th[9]/a"
    payment_type_sort_button = "//thead/tr[1]/th[10]/a"
    payment_system_sort_button = "//thead/tr[1]/th[11]/a"

    id_filter_field = "//tr[@id='w0-filters']/td[1]/input"
    phone_number_filter_field = "//tr[@id='w0-filters']/td[2]/input"
    companies_filter_button = "//tr[@id='w0-filters']/td[3]/span"
    sum_filter_field = "//tr[@id='w0-filters']/td[4]/input"
    date_first_filter_field = "//tr[@id='w0-filters']/td[5]/input[1]"
    date_second_filter_field = "//tr[@id='w0-filters']/td[5]/input[2]"
    comment_filter_field = "//tr[@id='w0-filters']/td[6]/input"
    category_filter_button = "//tr[@id='w0-filters']/td[7]/span"
    created_first_filter_field = "//tr[@id='w0-filters']/td[8]/input[1]"
    created_second_filter_field = "//tr[@id='w0-filters']/td[8]/input[2]"
    user_filter_button = "//tr[@id='w0-filters']/td[9]/span"
    payment_type_filter_select = "//tr[@id='w0-filters']/td[10]/select"
    payment_system_filter_select = "//tr[@id='w0-filters']/td[11]/select"

    span_filter_field = "//input[@type='search']"
    span_list_item = "//span[@class='select2-results']/ul/li"
