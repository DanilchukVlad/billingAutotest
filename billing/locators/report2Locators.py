class Report2Locators:

    # report2 urls
    report2_page_url = 'https://bill.bezlimit.ru/report/monitoring'
    report2_page_bill1_url = 'http://bill1.bezlimit.ru/report/monitoring'

    # report2 buttons123
    section_title = "//div[@class='panel-heading']/h3"
    reset_filters_title = "//div[@class='panel-control']/a"

    date_interval = "//div[@id='monitoring-grid']/b[3]"
    ban_filter_select = "//select[@id='monitoringsearch-partnerid']"

    # report2 sort buttons
    date_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[1]/a"
    all_payments_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[2]/a"
    bilain_payments_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[3]/a"
    sberbank_payments_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[4]/a"
    qiwi_payments_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[5]/a"
    sberbank_acquiring_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[6]/a"
    store_acquiring_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[8]/a"
    lk_acquiring_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[9]/a"
    site_acquiring_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[10]/a"
    store_payments_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[11]/a"
    cashless_payments_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[12]/a"
    group_number_payments_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[13]/a"
    refunds_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[15]/a"
    other_payments_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[16]/a"
    mkb_payments_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[17]/a"
    elecsnet_payments_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[18]/a"
    cyberplat_payments_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[19]/a"
    europlat_payments_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[20]/a"
    cash_payments_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[21]/a"
    promised_payments_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[22]/a"
    carried_over_payments_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[23]/a"
    payment_card_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[24]/a"
    other_accruals_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[25]/a"
    all_accruals_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[26]/a"
    hotbilling_accruals_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[27]/a"
    minus_extend_speed_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[28]/a"
    minus_cpa_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[29]/a"
    subscription_fee_accruals_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[31]/a"
    postpay_bills_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[32]/a"
    free_unlimited_connection_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[33]/a"
    activations_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[35]/a"
    false_activations_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[36]/a"
    activated_ffpa_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[37]/a"
    pd_sales_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[45]/a"
    pd_service_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[46]/a"
    quantity_active_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[38]/a"
    postpay_payments_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[40]/a"
    postpay_active_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[41]/a"
    prepay_payments_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[42]/a"
    prepay_active_sort_button = "//div[@id='monitoring-grid']/table/thead/tr/th[43]/a"

    span_filter_field = "//input[@type='search']"
    span_list_item = "//span[@class='select2-results']/ul/li"
