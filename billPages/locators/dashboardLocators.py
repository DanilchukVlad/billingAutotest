class DashboardLocators:

    dashboard_page_url = 'https://bill.bezlimit.ru/site/dashboard'
    dashboard_bill1_page_url = 'http://bill1.bezlimit.ru/site/dashboard'

    block_bloc = "//div[@id='w0']/div[@data-key='0']/div/div//div/p[1]"
    birthday_bloc = "//div[@id='w0']/div[@data-key='1']/div/div//div/p[1]"
    none_ban_bloc = "//div[@id='w0']/div[@data-key='2']/div/div//div/p[1]"
    none_ban_spartak_bloc = "//div[@id='w0']/div[@data-key='3']/div/div//div/p[1]"
    block_save_bloc = "//div[@id='w0']/div[@data-key='4']/div/div//div/p[1]"
    active_my1_bloc = "//div[@id='w0']/div[@data-key='5']/div/div//div/p[1]"
    guarantors_bloc = "//div[@id='w0']/div[@data-key='6']/div/div//div/p[1]"
    paid_blocking_bloc = "//div[@id='w0']/div[@data-key='7']/div/div//div/p[1]"
    booked_in_store_numbers_count = "//div[@id='w0']/div[@data-key='8']/div/div//div/p[1]"
    booked_in_store_dealers_count = "//div[@id='w0']/div[@data-key='8']/div/div//div/p[2]/br"
    numbers_in_store_all_count = "//div[@id='w0']/div[@data-key='9']/div/div//div/p[1]"
    numbers_in_store_paid_count = "//div[@id='w0']/div[@data-key='9']/div/div//div/p[2]/br[1]"
    numbers_in_store_internet_count = "//div[@id='w0']/div[@data-key='9']/div/div//div/p[2]/br[2]"
    pd_all_count = "//div[@id='w0']/div[@data-key='10']/div/div//div/p[1]"
    pd_ratio_count = "//div[@id='w0']/div[@data-key='10']/div/div//div/p[2]/br"

    statistic_bloc = "//div[@id='w1']/div[@data-key='0']/div/div//div/p[1]"
    timekeeper_button = "//div[@id='w1']/div[@data-key='1']/div/div//div"
    card_index_button = "//div[@id='w1']/div[@data-key='2']/div/div//div"
    cloud_button = "//div[@id='w1']/div[@data-key='3']/div/div//div"
    monitoring_button = "//div[@id='w1']/div[@data-key='4']/div/div//div"
    group_search_button = "//div[@id='w1']/div[@data-key='5']/div/div//div"
    search_by_package_button = "//div[@id='w1']/div[@data-key='6']/div/div//div"
    group_operations_button = "//div[@id='w1']/div[@data-key='7']/div/div//div"
    operations_with_packages_button = "//div[@id='w1']/div[@data-key='8']/div/div//div"
    reports_button = "//div[@id='w1']/div[@data-key='9']/div/div//div"

    export_to_excel_button = "//div[@id='w2']/div[@data-key='0']/div/div//div"
    archive_button = "//div[@id='w2']/div[@data-key='1']/div/div//div"
    passport_control_button = "//div[@id='w2']/div[@data-key='2']/div/div//div"
    hot_links_button = "//div[@id='w2']/div[@data-key='3']/div/div//div"
    incoming_button = "//div[@id='w2']/div[@data-key='4']/div/div//div"
    billing2_button = "//div[@id='w2']/div[@data-key='5']/div/div//div"
    renewal_agreement_button = "//div[@id='w2']/div[@data-key='6']/div/div//div"
    sdek_button = "//div[@id='w2']/div[@data-key='7']/div/div//div"

    store_button = "//div[@class='row']/div[1]/div[@class='panel media middle panel-colorful']"
    store_statistic_button = "//div[@class='row']/div[2]/div[@class='panel media middle panel-colorful']"
    site_button = "//div[@class='row']/div[3]/div[@class='panel media middle panel-colorful']"
    bitrix_button = "//div[@class='row']/div[4]/div[@class='panel media middle panel-colorful']"
    map_button = "//div[@class='row']/div[5]/div[@class='panel media middle panel-colorful']"
    problem_book_button = "//div[@class='row']/div[6]/div[@class='panel media middle panel-colorful']"
    forum_button = "//div[@class='row']/div[7]/div[@class='panel media middle panel-colorful']"
    beeline_button = "//div[@class='row']/div[8]/div[@class='panel media middle panel-colorful']"
    queues_cc_button = "//div[@class='row']/div[9]/div[@class='panel media middle panel-colorful']"
    guard_button = "//div[@class='row']/div[10]/div[@class='panel media middle panel-colorful']"

    active_monitoring_button = "//div[@class='row']/div[1]//a[@class='btn btn-default']"
    active_count_text = "//div[@class='row']/div[1]//div[@class='row']//span"
    active_refresh_button = "//div[@class='row']/div[1]//div[@class='row']//button"
    active_data_field = "//div[@class='row']/div[1]//div[@class='row']//input"

    activations_31report_button = "//div[@class='row']/div[2]//a[@class='btn btn-default']"
    activations_total_text = "//div[@class='row']/div[2]//div[@class='panel-body']/ul/li[1]/span"
    activations_store_text = "//div[@class='row']/div[2]//div[@class='panel-body']/ul/li[2]/span"
    activations_moscow_text = "//div[@class='row']/div[2]//div[@class='panel-body']/ul/li[3]/span"
    activations_regions_text = "//div[@class='row']/div[2]//div[@class='panel-body']/ul/li[4]/span"
    activations_refresh_button = "//div[@class='row']/div[2]//div[@class='row']//button"
    activations_first_date_field = "//div[@class='row']/div[2]//div[@class='row']/div[3]//input"
    activations_second_date_field = "//div[@class='row']/div[2]//div[@class='row']/div[2]//input"

    activations_today_31report_button = "//div[@class='row']/div[3]//a[@class='btn btn-default']"
    activations_today_total_text = "//div[@class='row']/div[3]//div[@class='panel-body']/ul/li[1]/span"
    activations_today_store_text = "//div[@class='row']/div[3]//div[@class='panel-body']/ul/li[2]/span"
    activations_today_moscow_text = "//div[@class='row']/div[3]//div[@class='panel-body']/ul/li[3]/span"
    activations_today_regions_text = "//div[@class='row']/div[3]//div[@class='panel-body']/ul/li[4]/span"
    activations_today_refresh_button = "//div[@class='row']/div[3]//div[@class='row']//button"
    activations_today_first_date_field = "//div[@class='row']/div[3]//div[@class='row']/div[3]//input"
    activations_today_second_date_field = "//div[@class='row']/div[3]//div[@class='row']/div[2]//input"