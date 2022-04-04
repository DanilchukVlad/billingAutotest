from billPages.methods.phoneCardMethods import PhoneCardMethods
import pytest


class Test:

    @pytest.mark.smoke
    def test_can_open_page_at_phone_card(self, browser):
        card = PhoneCardMethods(browser)

        card.go_to_phone_card_page(9602301639)

        card.authorization_at_billing()

        card.check_availability()
