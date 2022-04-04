class Report31Locators:
    report31_page_url = "https://bill.bezlimit.ru/report/activation"

    reset_filters_button = "//a[@class='btn btn-sm btn-purple btn-icon fal fa-filter']"
    show_disregarded_button = "//a[@class='btn btn-dark btn-sm btn-labeled fa fa-trash']"
    refixed_button = "//a[@class='btn btn-dark btn-sm btn-labeled fa fa-random']"
    export_button = "//a[@class='btn btn-success btn-sm btn-labeled fa fa-table']"
    export_pd_button = "//a[@class='btn btn-success btn-sm btn-labeled fa fa-users']"
    columns_button = "//button[@class='btn btn-sm btn-mint btn-labeled fa fa-cog']"

    number_of_records_total = "//div[@id='report-activations-grid']/div/b[2]"


    span_filter_field = "//input[@type='search']"
    span_list_item = "//span[@class='select2-results']/ul/li"
