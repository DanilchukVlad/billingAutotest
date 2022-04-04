from billPages.basePage import BasePage


class DashboardPage(BasePage):
    def __init__(self, browser):
        BasePage.__init__(self, browser)

        self.browser = browser

        self.dashboard_page_url = 'https://bill.bezlimit.ru/site/dashboard'

        self.block_button = "//div[@id='w0']/div[@data-key='0']/div/div//div/p[1]"
        self.birthday_text = "//div[@id='w0']/div[@data-key='1']/div/div//div/p[1]"
        self.none_ban_button = "//div[@id='w0']/div[@data-key='2']/div/div//div/p[1]"
        self.none_ban_spartak_button = "//div[@id='w0']/div[@data-key='3']/div/div//div/p[1]"
        self.block_save_button = "//div[@id='w0']/div[@data-key='4']/div/div//div/p[1]"
        self.active_my1_button = "//div[@id='w0']/div[@data-key='5']/div/div//div/p[1]"
        self.guarantors_button = "//div[@id='w0']/div[@data-key='6']/div/div//div/p[1]"
        self.paid_blocking_button = "//div[@id='w0']/div[@data-key='7']/div/div//div/p[1]"
        self.booked_in_store_text = "//div[@id='w0']/div[@data-key='8']/div/div//div/p[1]"
        self.numbers_in_store_text = "//div[@id='w0']/div[@data-key='9']/div/div//div/p[1]"
        self.pd_text = "//div[@id='w0']/div[@data-key='10']/div/div//div/p[1]"

        self.statistic_button = "//div[@id='w1']/div[@data-key='0']/div/div//div"
        self.timekeeper_button = "//div[@id='w1']/div[@data-key='1']/div/div//div"
        self.card_index_button = "//div[@id='w1']/div[@data-key='2']/div/div//div"
        self.cloud_button = "//div[@id='w1']/div[@data-key='3']/div/div//div"
        self.monitoring_button = "//div[@id='w1']/div[@data-key='4']/div/div//div"
        self.group_search_button = "//div[@id='w1']/div[@data-key='5']/div/div//div"
        self.search_by_package_button = "//div[@id='w1']/div[@data-key='6']/div/div//div"
        self.group_operations_button = "//div[@id='w1']/div[@data-key='7']/div/div//div"
        self.operations_with_packages_button = "//div[@id='w1']/div[@data-key='8']/div/div//div"
        self.reports_button = "//div[@id='w1']/div[@data-key='9']/div/div//div"

        self.export_to_excel_button = "//div[@id='w2']/div[@data-key='0']/div/div//div"
        self.archive_button = "//div[@id='w2']/div[@data-key='1']/div/div//div"
        self.passport_control_button = "//div[@id='w2']/div[@data-key='2']/div/div//div"
        self.hot_links_button = "//div[@id='w2']/div[@data-key='3']/div/div//div"
        self.incoming_button = "//div[@id='w2']/div[@data-key='4']/div/div//div"
        self.billing2_button = "//div[@id='w2']/div[@data-key='5']/div/div//div"
        self.renewal_agreement_button = "//div[@id='w2']/div[@data-key='6']/div/div//div"
        self.sdek_button = "//div[@id='w2']/div[@data-key='7']/div/div//div"

        self.store_button = "//div[@class='row']/div[1]/div[@class='panel media middle panel-colorful']"
        self.store_statistic_button = "//div[@class='row']/div[2]/div[@class='panel media middle panel-colorful']"
        self.site_button = "//div[@class='row']/div[3]/div[@class='panel media middle panel-colorful']"
        self.bitrix_button = "//div[@class='row']/div[4]/div[@class='panel media middle panel-colorful']"
        self.map_button = "//div[@class='row']/div[5]/div[@class='panel media middle panel-colorful']"
        self.problem_book_button = "//div[@class='row']/div[6]/div[@class='panel media middle panel-colorful']"
        self.forum_button = "//div[@class='row']/div[7]/div[@class='panel media middle panel-colorful']"
        self.beeline_button = "//div[@class='row']/div[8]/div[@class='panel media middle panel-colorful']"
        self.queues_cc_button = "//div[@class='row']/div[9]/div[@class='panel media middle panel-colorful']"
        self.guard_button = "//div[@class='row']/div[10]/div[@class='panel media middle panel-colorful']"

        self.active_monitoring_button = "//div[@class='row']/div[1]//a[@class='btn btn-default']"
        self.active_count_text = "//div[@class='row']/div[1]//div[@class='row']//span"
        self.active_refresh_button = "//div[@class='row']/div[1]//div[@class='row']//button"
        self.active_data_field = "//div[@class='row']/div[1]//div[@class='row']//input"

        self.activations_31report_button = "//div[@class='row']/div[2]//a[@class='btn btn-default']"
        self.activations_total_text = "//div[@class='row']/div[2]//div[@class='panel-body']/ul/li[1]/span"
        self.activations_store_text = "//div[@class='row']/div[2]//div[@class='panel-body']/ul/li[2]/span"
        self.activations_moscow_text = "//div[@class='row']/div[2]//div[@class='panel-body']/ul/li[3]/span"
        self.activations_regions_text = "//div[@class='row']/div[2]//div[@class='panel-body']/ul/li[4]/span"
        self.activations_refresh_button = "//div[@class='row']/div[2]//div[@class='row']//button"
        self.activations_first_date_field = "//div[@class='row']/div[2]//div[@class='row']/div[3]//input"
        self.activations_second_date_field = "//div[@class='row']/div[2]//div[@class='row']/div[2]//input"

        self.activations_today_31report_button = "//div[@class='row']/div[3]//a[@class='btn btn-default']"
        self.activations_today_total_text = "//div[@class='row']/div[3]//div[@class='panel-body']/ul/li[1]/span"
        self.activations_today_store_text = "//div[@class='row']/div[3]//div[@class='panel-body']/ul/li[2]/span"
        self.activations_today_moscow_text = "//div[@class='row']/div[3]//div[@class='panel-body']/ul/li[3]/span"
        self.activations_today_regions_text = "//div[@class='row']/div[3]//div[@class='panel-body']/ul/li[4]/span"
        self.activations_today_refresh_button = "//div[@class='row']/div[3]//div[@class='row']//button"
        self.activations_today_first_date_field = "//div[@class='row']/div[3]//div[@class='row']/div[3]//input"
        self.activations_today_second_date_field = "//div[@class='row']/div[3]//div[@class='row']/div[2]//input"

    def click_active_my1_button(self):
        self.browser.find_element_by_xpath(self.active_my1_button).click()
