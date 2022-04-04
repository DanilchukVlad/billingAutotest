class Report34QueueLocators:
    report34_page_url = 'https://bill.bezlimit.ru/report/sms-queue'

    reset_filters_button = "//a[@class='btn btn-sm btn-purple btn-icon fal fa-filter']"
    create_sms_button = "//a[@class='btn btn-sm btn-mint btn-labeled fal fa-plus']"

    archive_button = "//ul[@id='w1']/li[2]"

    number_of_records_total = "//div[@id='w0']/div/b[2]"

    id_sort_button = "//thead/tr/th[2]/a"
    phone_number_sort_button = "//thead/tr/th[3]/a"
    text_sort_button = "//thead/tr/th[5]/a"
    date_sending_sort_button = "//thead/tr/th[6]/a"
    status_queue_sort_button = "//thead/tr/th[7]/a"
    author_sort_button = "//thead/tr/th[8]/a"
    date_addition_sort_button = "//thead/tr/th[9]/a"
    id_smsru_sort_button = "//thead/tr/th[10]/a"
    status_smsru_sort_button = "//thead/tr/th[11]/a"
    type_message_sort_button = "//thead/tr/th[12]/a"
    channel_sort_button = "//thead/tr/th[14]/a"

    id_filter_field = "//tr[@id='w0-filters']/td[2]/input"
    phone_number_filter_field = "//tr[@id='w0-filters']/td[3]/input"
    companies_filter_button = "//tr[@id='w0-filters']/td[4]/span"
    text_filter_field = "//tr[@id='w0-filters']/td[5]/input"
    date_sending_first_filter_field = "//tr[@id='w0-filters']/td[6]/input[1]"
    date_sending_second_filter_field = "//tr[@id='w0-filters']/td[6]/input[2]"
    status_queue_filter_select = "//tr[@id='w0-filters']/td[7]/select"
    author_filter_button = "//tr[@id='w0-filters']/td[8]/span"
    date_addition_first_filter_field = "//tr[@id='w0-filters']/td[9]/input[1]"
    date_addition_second_filter_field = "//tr[@id='w0-filters']/td[9]/input[2]"
    id_smsru_filter_field = "//tr[@id='w0-filters']/td[10]/input"
    status_smsru_filter_select = "//tr[@id='w0-filters']/td[11]/select"
    type_message_filter_select = "//tr[@id='w0-filters']/td[12]/select"
    channel_filter_select = "//tr[@id='w0-filters']/td[14]/select"

    span_filter_field = "//input[@type='search']"
    span_list_item = "//span[@class='select2-results']/ul/li"
