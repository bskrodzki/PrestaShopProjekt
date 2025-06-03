from pages.base_page import BasePage
from locators.page_locators import ShippingPageLocators
from pages.bank_wire_payment_page import BankWirePaymentPage

class ShippingPage(BasePage):
    """
    Shipping Page
    """
    def click_terms_agree(self):
        el = self.driver.find_element(*ShippingPageLocators.TERMS_CHECKBOX)
        el.click()

    def click_proceed_to_checkout(self):
        el = self.driver.find_element(*ShippingPageLocators.PROCEED_TO_CHECKOUT)
        el.click()
        return BankWirePaymentPage(self.driver)