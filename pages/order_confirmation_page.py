from pages.base_page import BasePage
from locators.page_locators import OrderConfirmationPageLocators


class OrderConfirmationPage(BasePage):
    """
    Order Confirmation Page
    """
    def get_success_alert(self):
        el = self.driver.find_element(*OrderConfirmationPageLocators.ALERT_SUCCESS)
        assert el.text == "Your order on My Shop is complete.", \
            f"Oczekiwany komunikat 'Your order on My Shop is complete.', otrzymano: '{el.text}'"