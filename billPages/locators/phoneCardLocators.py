class PhoneCardLocators:
    phone_card_page_url = 'https://bill.bezlimit.ru/phone/card/view/'

    # navigation bar with tabs
    card_tab_button = "//ul[@id='w23']/li[1]"
    finance_tab_button = "//ul[@id='w23']/li[2]"
    services_tab_button = "//ul[@id='w23']/li[3]"
    queue_services_tab_button = "//ul[@id='w23']/li[4]"
    tasks_tab_button = "//ul[@id='w23']/li[5]"
    messages_tab_button = "//ul[@id='w23']/li[6]"
    log_tab_button = "//ul[@id='w23']/li[7]"
    archive_log_tab_button = "//ul[@id='w23']/li[8]"
    history_tab_button = "//ul[@id='w23']/li[9]"
    passport_log_button = "//ul[@id='w23']/li[10]"

    # left panel
    # tariff block
    tariff_block = "//div[@id='panel-tariff']"
    name_tariff_link = "//div[@id='panel-tariff']/div[1]/h4/a"
    change_tariff_button = "//div[@id='panel-tariff']/div[1]/div/div/a[1]"
    description_tariff_button = "//div[@id='panel-tariff']/div[1]/div/div/a[2]"
    recommendations_tariff_button = "//div[@id='panel-tariff']/div[1]/div/div/a[3]"
    collapse_block_tariff_button = "//div[@id='panel-tariff']/div[1]/div/button"

    # roaming block
    roaming_block = "//div[@id='panel-roaming']"
    collapse_block_roaming_button = "//div[@id='panel-roaming']/div[1]/div/button"

    # fake-tariff block
    fake_tariff_block = "//div[@id='panel-fake-tariff']"
    collapse_block_fake_tariff_button = "//div[@id='panel-fake-tariff']/div[1]/div/button"

    # mask block
    mask_block = "//div[@id='panel-mask']"
    collapse_block_mask_button = "//div[@id='panel-mask']/div[1]/div/button"

    # sim block
    sim_block = "//div[@id='panel-sim']"
    collapse_block_sim_button = "//div[@id='panel-sim']/div[1]/div/button"

    # keeper block
    keeper_block = "//div[@id='panel-keeper']"
    collapse_block_keeper_button = "//div[@id='panel-keeper']/div[1]/div/button"

    # center panel
    # juridical block
    juridical_block = "//div[@id='panel-juridical']"
    collapse_block_juridical_button = "//div[@id='panel-juridical']/div[1]/div/button"

    # activation block
    activation_block = "//div[@id='panel-activation']"
    collapse_block_activation_button = "//div[@id='panel-activation']/div[1]/div/button"

    # other block
    other_block = "//div[@id='panel-other']"
    collapse_block_other_button = "//div[@id='panel-other']/div[1]/div/button"

    # right panel
    # pd block
    pd_block = "//div[@id='panel-pd']"
    collapse_block_pd_button = "//div[@id='panel-pd']/div[1]/div/button[3]"

    # rests block
    rests_block = "//div[@id='panel-rests']"
    collapse_block_rests_button = "//div[@id='panel-rests']/div[1]/div/button"

    # minutes block
    minutes_block = "//div[@id='panel-minutes']"
    collapse_block_minutes_button = "//div[@id='panel-minutes']/div[1]/div/button"

    # sms block
    sms_block = "//div[@id='panel-sms']"
    collapse_block_sms_button = "//div[@id='panel-sms']/div[1]/div/button"

    # internet
    internet_block = "//div[@id='panel-internet']"
    collapse_block_internet_button = "//div[@id='panel-internet']/div[1]/div/button"

    # notify block
    notify_block = "//div[@id='panel-notify']"
    collapse_block_notify_button = "//div[@id='panel-notify']/div[1]/div/button"

    # deferred block
    deferred_block = "//div[@id='panel-deferred']"
    collapse_block_deferred_button = "//div[@id='panel-deferred']/div[1]/div/button[3]"

    # statistic block
    statistic_block = "//div[@id='panel-statistics']"
    collapse_block_statistic_button = "//div[@id='panel-statistics']/div[1]/div/button[2]"
