from pages.base_page import BasePage
from locators.page_locators import BankWirePaymentPageLocators
from pages.order_confirmation_page import OrderConfirmationPage

class BankWirePaymentPage(BasePage):
    """
    Bank Wire Payment Page
    """
    def click_confirm_order(self):
        el = self.driver.find_element(*BankWirePaymentPageLocators.CONFIRM_ORDER)
        el.click()
        return  OrderConfirmationPage(self.driver)