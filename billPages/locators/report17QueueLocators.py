class Report17QueueLocators:

    report17_queue_page_url = 'https://bill.bezlimit.ru/report/change-tariff/queue'

    reset_filters_button = "//a[@class='btn btn-sm btn-purple btn-icon fal fa-filter']"
    export_button = "//a[@class='btn btn-success btn-sm btn-labeled fal fa-table']"
    download_xls_button = "//form[@id='w0']"

    number_of_records_total = "//div[@id='w1']/div/b[2]"

    '''id_sort_button = "//thead/tr[1]/th[1]/a"
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
    date_created_second_filter_field = "//tr[@id='w0-filters']/td[13]/input[2]"'''

    span_filter_field = "//input[@type='search']"
    span_list_item = "//span[@class='select2-results']/ul/li"
