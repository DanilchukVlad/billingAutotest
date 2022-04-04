import datetime as dt


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        # Navbar
        self.navbar = "//header"

        self.home_button_nav = "//ul[@class='nav navbar-top-links pull-left']/li[1]"

        self.base_button_nav = "//ul[@class='nav navbar-top-links pull-left']/li[2]"

        self.finance_button_nav = "//ul[@class='nav navbar-top-links pull-left']/li[3]"
        self.payments_button_nav = "//li[@class='dropdown open']//li[1]"
        self.accruals_button_nav = "//li[@class='dropdown open']//li[2]"
        self.commission_button_nav = "//li[@class='dropdown open']//li[3]"
        self.rebound_contracts_button_nav = "//li[@class='dropdown open']//li[4]"

        self.tariffs_button_nav = "//ul[@class='nav navbar-top-links pull-left']/li[4]"
        self.false_packages_button_nav = "//div[@class='col-sm-3 col-md-2'][1]/ul[@class='list-unstyled'][2]/li[1]"
        self.rules_of_false_packages_button_nav = \
            "//div[@class='col-sm-3 col-md-2'][1]/ul[@class='list-unstyled'][2]/li[2]"
        self.tariff_lines_button_nav = "//div[@class='col-sm-3 col-md-2'][2]/ul[@class='list-unstyled'][2]/li[1]"
        self.tariff_plans_button_nav = "//div[@class='col-sm-3 col-md-2'][2]/ul[@class='list-unstyled'][2]/li[2]"
        self.services_button_nav = "//div[@class='col-sm-3 col-md-2'][2]/ul[@class='list-unstyled'][2]/li[3]"
        self.parameters_button_nav = "//div[@class='col-sm-3 col-md-2'][2]/ul[@class='list-unstyled'][2]/li[4]"
        self.description_templates_button_nav = \
            "//div[@class='col-sm-3 col-md-2'][2]/ul[@class='list-unstyled'][2]/li[5]"
        self.restrictions_shares_button_nav = "//div[@class='col-sm-3 col-md-2'][3]/ul[@class='list-unstyled'][2]/li[1]"
        self.min_tariff_restrictions_button_nav = \
            "//div[@class='col-sm-3 col-md-2'][3]/ul[@class='list-unstyled'][2]/li[2]"
        self.default_tariff_button_nav = "//div[@class='col-sm-3 col-md-2'][3]/ul[@class='list-unstyled'][2]/li[3]"
        self.export_tariff_button_nav = "//div[@class='col-sm-3 col-md-2'][3]/ul[@class='list-unstyled'][2]/li[4]"

        self.dealers_button_nav = "//ul[@class='nav navbar-top-links pull-left']/li[5]"
        self.dealers_dealers_button_nav = "//li[@class='dropdown open']//li[1]"
        self.create_dealers_button_nav = "//li[@class='dropdown open']//li[2]"
        self.classification_button_nav = "//li[@class='dropdown open']//li[3]"

        self.tasks_button_nav = "//ul[@class='nav navbar-top-links pull-left']/li[6]"

        self.orders_button_nav = "//ul[@class='nav navbar-top-links pull-left']/li[7]"
        self.all_orders_button_nav = "//li[@class='dropdown open']//li[1]"
        self.current_orders_button_nav = "//li[@class='dropdown open']//li[2]"
        self.mail_button_nav = "//li[@class='dropdown open']//li[3]"
        self.pickup_button_nav = "//li[@class='dropdown open']//li[4]"

        self.storage_button_nav = "//ul[@class='nav navbar-top-links pull-left']/li[8]"
        self.cloud_button_nav = "//li[@class='dropdown open']//li[1]"
        self.reissue_button_nav = "//li[@class='dropdown open']//li[2]"
        self.mask_button_nav = "//li[@class='dropdown open']//li[3]"
        self.mask_category_button_nav = "//li[@class='dropdown open']//li[4]"
        self.save_button_nav = "//li[@class='dropdown open']//li[5]"
        self.task_queue_button_nav = "//li[@class='dropdown open']//li[6]"
        self.labels_button_nav = "//li[@class='dropdown open']//li[7]"
        self.booking_button_nav = "//li[@class='dropdown open']//li[8]"
        self.frod_button_nav = "//li[@class='dropdown open']//li[9]"

        self.tools_button_nav = "//ul[@class='nav navbar-top-links pull-left']/li[9]"
        self.group_operations_button_nav = "//li[@class='dropdown open']//li[1]"
        self.passports_button_nav = "//li[@class='dropdown open']//li[2]"
        self.number_signs_button_nav = "//li[@class='dropdown open']//li[3]"
        self.spartak_lottery_button_nav = "//li[@class='dropdown open']//li[4]"

        self.reports_button_nav = "//ul[@class='nav navbar-top-links pull-left']/li[10]"
        self.all_reports_button_nav = "//li[10]//div[@class='col-sm-3 col-md-2'][1]//li[1]"
        self.ban_settings_button_nav = "//li[10]//div[@class='col-sm-3 col-md-2'][1]//li[2]"
        self.month_statistic_button_nav = "//li[10]//div[@class='col-sm-3 col-md-2'][1]//li[3]"
        self.report1_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[1]/div"
        self.report2_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[2]/div"
        self.report3_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[3]/div"
        self.report4_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[4]/div"
        self.report5_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[5]/div"
        self.report6_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[6]/div"
        self.report7_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[7]/div"
        self.report8_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[8]/div"
        self.report9_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[9]/div"
        self.report10_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[10]/div"
        self.report11_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[11]/div"
        self.report12_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[12]/div"
        self.report13_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[13]/div"
        self.report14_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[14]/div"
        self.report15_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[15]/div"
        self.report16_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[16]/div"
        self.report17_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[17]/div"
        self.report18_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[18]/div"
        self.report19_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[19]/div"
        self.report20_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[20]/div"
        self.report21_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[21]/div"
        self.report22_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[22]/div"
        self.report23_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[23]/div"
        self.report24_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[24]/div"
        self.report25_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[25]/div"
        self.report26_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[26]/div"
        self.report27_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[27]/div"
        self.report28_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[28]/div"
        self.report29_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[29]/div"
        self.report30_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[30]/div"
        self.report31_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[31]/div"
        self.report32_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[32]/div"
        self.report33_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[33]/div"
        self.report34_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[34]/div"
        self.report35_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[35]/div"
        self.report36_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[36]/div"
        self.report37_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[37]/div"
        self.report38_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[38]/div"
        self.report39_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[39]/div"
        self.report40_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[40]/div"
        self.report41_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[41]/div"
        self.report42_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[42]/div"
        self.report43_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[43]/div"
        self.report44_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[44]/div"
        self.report45_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[45]/div"
        self.report46_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[46]/div"
        self.report47_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[47]/div"
        self.report48_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[48]/div"
        self.report49_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[49]/div"
        self.report50_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[50]/div"
        self.report51_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[51]/div"
        self.report52_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[52]/div"
        self.report53_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[53]/div"
        self.report54_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[54]/div"
        self.report55_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[55]/div"
        self.report56_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[56]/div"
        self.report57_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[57]/div"
        self.report58_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[58]/div"
        self.report59_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[59]/div"
        self.report60_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[60]/div"
        self.report61_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[61]/div"
        self.report62_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[62]/div"
        self.report63_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[63]/div"
        self.report64_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[64]/div"
        self.report65_button_nav = "//li[10]//div[@class='col-sm-9 col-md-10']/div[65]/div"

        self.admin_button_nav = "//ul[@class='nav navbar-top-links pull-left']/li[11]"
        self.timekeeper_button_nav = "//li[11]//div/div[@class='row']/div[1]//li[1]"
        self.timetable_button_nav = "//li[11]//div/div[@class='row']/div[1]//li[2]"
        self.personal_adjustments_button_nav = "//li[11]//div/div[@class='row']/div[1]//li[3]"
        self.visit_log_button_nav = "//li[11]//div/div[@class='row']/div[1]//li[4]"
        self.timekeeper_report_button_nav = "//li[11]//div/div[@class='row']/div[1]//li[5]"
        self.ban_accounts_button_nav = "//li[11]//div/div[@class='row']/div[2]//li[1]"
        self.access_rights_button_nav = "//li[11]//div/div[@class='row']/div[2]//li[2]"
        self.vacation_button_nav = "//li[11]//div/div[@class='row']/div[2]//li[3]"
        self.ats_button_nav = "//li[11]//div/div[@class='row']/div[2]//li[4]"
        self.roles_button_nav = "//li[11]//div/div[@class='row']/div[3]//li[1]"
        self.permission_button_nav = "//li[11]//div/div[@class='row']/div[3]//li[2]"
        self.routes_button_nav = "//li[11]//div/div[@class='row']/div[3]//li[3]"
        self.exceptions_button_nav = "//li[11]//div/div[@class='row']/div[3]//li[4]"
        self.tk_event_log_button_nav = "//li[11]//div/div[@class='row']/div[4]//li[1]"
        self.area_codes_button_nav = "//li[11]//div/div[@class='row']/div[4]//li[2]"
        self.accounts_button_nav = "//li[11]//div/div[@class='row']/div[5]//li[1]"

        self.twins_button_nav = "//ul[@class='nav navbar-top-links pull-left']/li[11]"
        self.control_panel_button_nav = "//li[@class='dropdown open']//li[1]"
        self.storage_twins_button_nav = "//li[@class='dropdown open']//li[2]"
        self.dealers_exceptions_button_nav = "//li[@class='dropdown open']//li[3]"

        self.card_index_button_nav = "//ul[@class='nav navbar-top-links pull-left']/li[13]"

        self.callcenter_button_nav = "//ul[@class='nav navbar-top-links pull-left']/li[14]"
        self.incoming_button_nav = "//li[@class='dropdown open']//li[1]"
        self.categories_button_nav = "//li[@class='dropdown open']//li[2]"
        self.appeal_button_nav = "//li[@class='dropdown open']//li[3]"
        self.solutions_button_nav = "//li[@class='dropdown open']//li[4]"
        self.qc_incoming_button_nav = "//li[@class='dropdown open']//li[5]"
        self.qc_topics_button_nav = "//li[@class='dropdown open']//li[6]"
        self.qc_reasons_button_nav = "//li[@class='dropdown open']//li[7]"

        self.cashless_button_nav = "//ul[@class='nav navbar-top-links pull-left']/li[15]"

        self.phone_search_button_nav = "//ul[@class='nav pull-right']"
        self.phone_search_field_nav = "//input[@class='select2-search__field']"
        self.phone_number_button_nav = "//li[@class='select2-results__option']"

        self.profile_button_nav = "//ul[@class='nav navbar-top-links pull-right']/li"
        self.my_profile_button_nav = "//ul[@class='nav navbar-top-links pull-right']/li//li[1]"
        self.change_password_button_nav = "//ul[@class='nav navbar-top-links pull-right']/li//li[2]"
        self.exit_button_nav = "//ul[@class='nav navbar-top-links pull-right']/li//li[3]"

    def check_accessibility(self):
        assert self.browser.find_element_by_xpath(self.navbar)

    def click_home_button_nav(self):
        self.browser.find_element_by_xpath(self.home_button_nav).click()

    def click_base_button_nav(self):
        self.browser.find_element_by_xpath(self.base_button_nav).click()

    def click_finance_button_nav(self):
        self.browser.find_element_by_xpath(self.finance_button_nav).click()

    def click_payments_button_nav(self):
        self.click_finance_button_nav()
        self.browser.find_element_by_xpath(self.payments_button_nav).click()

    def click_accruals_button_nav(self):
        self.click_finance_button_nav()
        self.browser.find_element_by_xpath(self.accruals_button_nav).click()

    def click_commission_button_nav(self):
        self.click_finance_button_nav()
        self.browser.find_element_by_xpath(self.commission_button_nav).click()

    def click_rebound_contracts_button_nav(self):
        self.click_finance_button_nav()
        self.browser.find_element_by_xpath(self.rebound_contracts_button_nav).click()

    def click_tariffs_button_nav(self):
        self.browser.find_element_by_xpath(self.tariffs_button_nav).click()

    def click_false_packages_button_nav(self):
        self.click_tariffs_button_nav()
        self.browser.find_element_by_xpath(self.false_packages_button_nav).click()

    def click_rules_of_false_packages_button_nav(self):
        self.click_tariffs_button_nav()
        self.browser.find_element_by_xpath(self.rules_of_false_packages_button_nav).click()

    def click_tariff_lines_button_nav(self):
        self.click_tariffs_button_nav()
        self.browser.find_element_by_xpath(self.tariff_lines_button_nav).click()

    def click_tariff_plans_button_nav(self):
        self.click_tariffs_button_nav()
        self.browser.find_element_by_xpath(self.tariff_plans_button_nav).click()

    def click_services_button_nav(self):
        self.click_tariffs_button_nav()
        self.browser.find_element_by_xpath(self.services_button_nav).click()

    def click_parameters_button_nav(self):
        self.click_tariffs_button_nav()
        self.browser.find_element_by_xpath(self.parameters_button_nav).click()

    def click_description_templates_button_nav(self):
        self.click_tariffs_button_nav()
        self.browser.find_element_by_xpath(self.description_templates_button_nav).click()

    def click_restrictions_shares_button_nav(self):
        self.click_tariffs_button_nav()
        self.browser.find_element_by_xpath(self.restrictions_shares_button_nav).click()

    def click_min_tariff_restrictions_button_nav(self):
        self.click_tariffs_button_nav()
        self.browser.find_element_by_xpath(self.min_tariff_restrictions_button_nav).click()

    def click_default_tariff_button_nav(self):
        self.click_tariffs_button_nav()
        self.browser.find_element_by_xpath(self.default_tariff_button_nav).click()

    def click_export_tariff_button_nav(self):
        self.click_tariffs_button_nav()
        self.browser.find_element_by_xpath(self.export_tariff_button_nav).click()

    def click_dealers_button_nav(self):
        self.browser.find_element_by_xpath(self.dealers_button_nav).click()

    def click_dealers_dealers_button_nav(self):
        self.click_dealers_button_nav()
        self.browser.find_element_by_xpath(self.dealers_dealers_button_nav).click()

    def click_create_dealers_button_nav(self):
        self.click_dealers_button_nav()
        self.browser.find_element_by_xpath(self.create_dealers_button_nav).click()

    def click_classification_button_nav(self):
        self.click_dealers_button_nav()
        self.browser.find_element_by_xpath(self.classification_button_nav).click()

    def click_tasks_button_nav(self):
        self.browser.find_element_by_xpath(self.tasks_button_nav).click()

    def click_orders_button_nav(self):
        self.browser.find_element_by_xpath(self.orders_button_nav).click()

    def click_all_orders_button_nav(self):
        self.click_orders_button_nav()
        self.browser.find_element_by_xpath(self.all_orders_button_nav).click()

    def click_current_orders_button_nav(self):
        self.click_orders_button_nav()
        self.browser.find_element_by_xpath(self.current_orders_button_nav).click()

    def click_mail_button_nav(self):
        self.click_orders_button_nav()
        self.browser.find_element_by_xpath(self.mail_button_nav).click()

    def click_pickup_button_nav(self):
        self.click_orders_button_nav()
        self.browser.find_element_by_xpath(self.pickup_button_nav).click()

    def click_storage_button_nav(self):
        self.browser.find_element_by_xpath(self.storage_button_nav).click()

    def click_cloud_button_nav(self):
        self.click_storage_button_nav()
        self.browser.find_element_by_xpath(self.cloud_button_nav).click()

    def click_reissue_button_nav(self):
        self.click_storage_button_nav()
        self.browser.find_element_by_xpath(self.reissue_button_nav).click()

    def click_mask_button_nav(self):
        self.click_storage_button_nav()
        self.browser.find_element_by_xpath(self.mask_button_nav).click()

    def click_mask_category_button_nav(self):
        self.click_storage_button_nav()
        self.browser.find_element_by_xpath(self.mask_category_button_nav).click()

    def click_save_button_nav(self):
        self.click_storage_button_nav()
        self.browser.find_element_by_xpath(self.save_button_nav).click()

    def click_task_queue_button_nav(self):
        self.click_storage_button_nav()
        self.browser.find_element_by_xpath(self.task_queue_button_nav).click()

    def click_labels_button_nav(self):
        self.click_storage_button_nav()
        self.browser.find_element_by_xpath(self.labels_button_nav).click()

    def click_booking_button_nav(self):
        self.click_storage_button_nav()
        self.browser.find_element_by_xpath(self.booking_button_nav).click()

    def click_frod_button_nav(self):
        self.click_storage_button_nav()
        self.browser.find_element_by_xpath(self.frod_button_nav).click()

    def click_tools_button_nav(self):
        self.browser.find_element_by_xpath(self.tools_button_nav).click()

    def click_group_operations_button_nav(self):
        self.click_tools_button_nav()
        self.browser.find_element_by_xpath(self.group_operations_button_nav).click()

    def click_passports_button_nav(self):
        self.click_tools_button_nav()
        self.browser.find_element_by_xpath(self.passports_button_nav).click()

    def click_numbers_signs_button_nav(self):
        self.click_tools_button_nav()
        self.browser.find_element_by_xpath(self.number_signs_button_nav).click()

    def click_spartak_lottery_button_nav(self):
        self.click_tools_button_nav()
        self.browser.find_element_by_xpath(self.spartak_lottery_button_nav).click()

    def click_reports_button_nav(self):
        self.browser.find_element_by_xpath(self.reports_button_nav).click()

    def click_all_reports_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.all_reports_button_nav).click()

    def click_ban_settings_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.ban_settings_button_nav).click()

    def click_month_statistic_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.month_statistic_button_nav).click()

    def click_report1_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report1_button_nav).click()

    def click_report2_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report2_button_nav).click()

    def click_report3_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report3_button_nav).click()

    def click_report4_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report4_button_nav).click()

    def click_report5_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report5_button_nav).click()

    def click_report6_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report6_button_nav).click()

    def click_report7_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report7_button_nav).click()

    def click_report8_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report8_button_nav).click()

    def click_report9_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report9_button_nav).click()

    def click_report10_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report10_button_nav).click()

    def click_report11_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report11_button_nav).click()

    def click_report12_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report12_button_nav).click()

    def click_report13_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report13_button_nav).click()

    def click_report14_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report14_button_nav).click()

    def click_report15_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report15_button_nav).click()

    def click_report16_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report16_button_nav).click()

    def click_report17_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report17_button_nav).click()

    def click_report18_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report18_button_nav).click()

    def click_report19_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report19_button_nav).click()

    def click_report20_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report20_button_nav).click()

    def click_report21_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report21_button_nav).click()

    def click_report22_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report22_button_nav).click()

    def click_report23_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report23_button_nav).click()

    def click_report24_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report24_button_nav).click()

    def click_report25_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report25_button_nav).click()

    def click_report26_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report26_button_nav).click()

    def click_report27_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report27_button_nav).click()

    def click_report28_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report28_button_nav).click()

    def click_report29_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report29_button_nav).click()

    def click_report30_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report30_button_nav).click()

    def click_report31_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report31_button_nav).click()

    def click_report32_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report32_button_nav).click()

    def click_report33_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report33_button_nav).click()

    def click_report34_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report34_button_nav).click()

    def click_report35_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report35_button_nav).click()

    def click_report36_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report36_button_nav).click()

    def click_report37_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report37_button_nav).click()

    def click_report38_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report38_button_nav).click()

    def click_report39_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report39_button_nav).click()

    def click_report40_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report40_button_nav).click()

    def click_report41_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report41_button_nav).click()

    def click_report42_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report42_button_nav).click()

    def click_report43_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report43_button_nav).click()

    def click_report44_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report44_button_nav).click()

    def click_report45_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report45_button_nav).click()

    def click_report46_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report46_button_nav).click()

    def click_report47_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report47_button_nav).click()

    def click_report48_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report48_button_nav).click()

    def click_report49_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report49_button_nav).click()

    def click_report50_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report50_button_nav).click()

    def click_report51_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report51_button_nav).click()

    def click_report52_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report52_button_nav).click()

    def click_report53_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report53_button_nav).click()

    def click_report54_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report54_button_nav).click()

    def click_report55_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report55_button_nav).click()

    def click_report56_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report56_button_nav).click()

    def click_report57_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report57_button_nav).click()

    def click_report58_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report58_button_nav).click()

    def click_report59_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report59_button_nav).click()

    def click_report60_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report60_button_nav).click()

    def click_report61_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report61_button_nav).click()

    def click_report62_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report62_button_nav).click()

    def click_report63_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report63_button_nav).click()

    def click_report64_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report64_button_nav).click()

    def click_report65_button_nav(self):
        self.click_reports_button_nav()
        self.browser.find_element_by_xpath(self.report65_button_nav).click()

    def click_admin_button_nav(self):
        self.browser.find_element_by_xpath(self.admin_button_nav).click()

    def click_timekeeper_button_nav(self):
        self.click_admin_button_nav()
        self.browser.find_element_by_xpath(self.timekeeper_button_nav).click()

    def click_timetable_button_nav(self):
        self.click_admin_button_nav()
        self.browser.find_element_by_xpath(self.timetable_button_nav).click()

    def click_personal_adjustments_button_nav(self):
        self.click_admin_button_nav()
        self.browser.find_element_by_xpath(self.personal_adjustments_button_nav).click()

    def click_visit_log_button_nav(self):
        self.click_admin_button_nav()
        self.browser.find_element_by_xpath(self.visit_log_button_nav).click()

    def click_timekeeper_report_button_nav(self):
        self.click_admin_button_nav()
        self.browser.find_element_by_xpath(self.timekeeper_report_button_nav).click()

    def click_ban_accounts_button_nav(self):
        self.click_admin_button_nav()
        self.browser.find_element_by_xpath(self.ban_accounts_button_nav).click()

    def click_access_rights_button_nav(self):
        self.click_admin_button_nav()
        self.browser.find_element_by_xpath(self.access_rights_button_nav).click()

    def click_vacation_button_nav(self):
        self.click_admin_button_nav()
        self.browser.find_element_by_xpath(self.vacation_button_nav).click()

    def click_ats_button_nav(self):
        self.click_admin_button_nav()
        self.browser.find_element_by_xpath(self.ats_button_nav).click()

    def click_roles_button_nav(self):
        self.click_admin_button_nav()
        self.browser.find_element_by_xpath(self.roles_button_nav).click()

    def click_permission_button_nav(self):
        self.click_admin_button_nav()
        self.browser.find_element_by_xpath(self.permission_button_nav).click()

    def click_routes_button_nav(self):
        self.click_admin_button_nav()
        self.browser.find_element_by_xpath(self.routes_button_nav).click()

    def click_exceptions_button_nav(self):
        self.click_admin_button_nav()
        self.browser.find_element_by_xpath(self.exceptions_button_nav).click()

    def click_tk_event_log_button_nav(self):
        self.click_admin_button_nav()
        self.browser.find_element_by_xpath(self.tk_event_log_button_nav).click()

    def click_area_codes_button_nav(self):
        self.click_admin_button_nav()
        self.browser.find_element_by_xpath(self.area_codes_button_nav).click()

    def click_accounts_button_nav(self):
        self.click_admin_button_nav()
        self.browser.find_element_by_xpath(self.accounts_button_nav).click()

    def click_twins_button_nav(self):
        self.browser.find_element_by_xpath(self.twins_button_nav).click()

    def click_control_panel_button_nav(self):
        self.click_twins_button_nav()
        self.browser.find_element_by_xpath(self.control_panel_button_nav).click()

    def click_storage_twins_button_nav(self):
        self.click_twins_button_nav()
        self.browser.find_element_by_xpath(self.storage_twins_button_nav).click()

    def click_dealers_exceptions_button_nav(self):
        self.click_twins_button_nav()
        self.browser.find_element_by_xpath(self.dealers_exceptions_button_nav).click()

    def click_card_index_button_nav(self):
        self.browser.find_element_by_xpath(self.card_index_button_nav).click()

    def click_callcenter_button_nav(self):
        self.browser.find_element_by_xpath(self.callcenter_button_nav).click()

    def click_incoming_button_nav(self):
        self.click_callcenter_button_nav()
        self.browser.find_element_by_xpath(self.incoming_button_nav).click()

    def click_categories_button_nav(self):
        self.click_callcenter_button_nav()
        self.browser.find_element_by_xpath(self.categories_button_nav).click()

    def click_appeal_button_nav(self):
        self.click_callcenter_button_nav()
        self.browser.find_element_by_xpath(self.appeal_button_nav).click()

    def click_solutions_button_nav(self):
        self.click_callcenter_button_nav()
        self.browser.find_element_by_xpath(self.solutions_button_nav).click()

    def click_qc_incoming_button_nav(self):
        self.click_callcenter_button_nav()
        self.browser.find_element_by_xpath(self.qc_incoming_button_nav).click()

    def click_qc_topics_button_nav(self):
        self.click_callcenter_button_nav()
        self.browser.find_element_by_xpath(self.qc_topics_button_nav).click()

    def click_qc_reasons_button_nav(self):
        self.click_callcenter_button_nav()
        self.browser.find_element_by_xpath(self.qc_reasons_button_nav).click()

    def click_cashless_button_nav(self):
        self.browser.find_element_by_xpath(self.cashless_button_nav).click()

    def click_phone_search_button_nav(self):
        self.browser.find_element_by_xpath(self.phone_search_button_nav).click()

    def enter_phone_number(self, phone_number: int):
        self.click_phone_search_button_nav()
        self.browser.find_element_by_xpath(self.phone_search_field_nav).clear()
        self.browser.find_element_by_xpath(self.phone_search_field_nav).send_keys(phone_number)

    def choose_phone_number(self, number=1):
        self.browser.find_element_by_xpath(self.phone_number_button_nav + '[' + str(number) + ']').click()

    def click_profile_button_nav(self):
        self.browser.find_element_by_xpath(self.profile_button_nav).click()

    def click_my_profile_button_nav(self):
        self.click_profile_button_nav()
        self.browser.find_element_by_xpath(self.my_profile_button_nav).click()

    def click_change_password_button_nav(self):
        self.click_profile_button_nav()
        self.browser.find_element_by_xpath(self.change_password_button_nav).click()

    def click_exit_button_nav(self):
        self.click_profile_button_nav()
        self.browser.find_element_by_xpath(self.exit_button_nav).click()

    def calculate_time_difference(self, time_delta=30, read_time="1980-01-01 00:00:00"):
        now = dt.datetime.now()
        delta = dt.timedelta(minutes=time_delta)
        time = dt.datetime.strptime(read_time, '%Y-%m-%d %H:%M:%S')
        if now-time > delta:
            return True
        else:
            return False
