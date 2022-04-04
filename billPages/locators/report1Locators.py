class Report1Locators:

    # report1 urls
    report1_page_url = 'https://bill.bezlimit.ru/report/phone-queue'

    # report1 buttons
    reset_filters_button = "//div[@class='panel-control']/a"

    # report1 tabs
    queue_tab_button = "//ul[@id='w1']/li[1]"
    change_status_tab_button = "//ul[@id='w1']/li[2]"
    change_sim_tab_button = "//ul[@id='w1']/li[3]"

    number_of_records_total = "//div[@id='w0']/div/b[2]"

    # Sort buttons
    id_checkbox = "//thead/tr/th[1]/a"
    phone_number_sort_button = "//thead/tr/th[2]/a"
    status_sort_button = "//thead/tr/th[4]/a"
    service_code_sort_button = "//thead/tr/th[5]/a"
    new_sim_number_sort_button = "//thead/tr/th[6]/a"
    related_task_sort_button = "//thead/tr/th[7]/a"
    task_source_sort_button = "//thead/tr/th[8]/a"
    queue_status_sort_button = "//thead/tr/th[9]/a"
    response_code_sort_button = "//thead/tr/th[10]/a"
    response_number_sort_button = "//thead/tr/th[11]/a"
    control_check_sort_button = "//thead/tr/th[12]/a"
    date_creation_sort_button = "//thead/tr/th[13]/a"
    date_update_sort_button = "//thead/tr/th[14]/a"
    author_sort_button = "//thead/tr/th[15]/a"
    status_hand_sort_button = "//thead/tr/th[16]/a"

    # Filters
    id_filter_field = "//tr[@id='w0-filters']/td[1]/input"
    phone_number_filter_field = "//tr[@id='w0-filters']/td[2]/input"
    company_filter_button = "//tr[@id='w0-filters']/td[3]/span"
    status_filter_select = "//tr[@id='w0-filters']/td[4]/select"
    service_code_filter_field = "//tr[@id='w0-filters']/td[5]/input"
    new_sim_number_filter_field = "//tr[@id='w0-filters']/td[6]/input"
    related_task_filter_field = "//tr[@id='w0-filters']/td[7]/input"
    task_source_filter_field = "//tr[@id='w0-filters']/td[8]/input"

    queue_status_filter_select = "//tr[@id='w0-filters']/td[9]/select"

    response_code_filter_field = "//thead/tr/th[10]/a"
    response_number_filter_field = "//thead/tr/th[11]/a"
    control_check_filter_field = "//thead/tr/th[12]/a"
    date_creation_filter_field = "//thead/tr/th[13]/a"
    date_update_filter_field = "//thead/tr/th[14]/a"
    author_filter_field = "//thead/tr/th[15]/a"
    status_hand_filter_field = "//thead/tr/th[16]/a"

    span_filter_field = "//input[@type='search']"
    span_list_item = "//span[@class='select2-results']/ul/li"
