from pages.base_page import BasePage
from locators.page_locators import YourPaymentMethodPageLocators
from pages.bank_wire_payment_page import BankWirePaymentPage

class YourPaymentMethodPage(BasePage):
    def click_pay_by_bank(self):
        """
        Your Payment Method Page
        """
        el = self.driver.find_element(*YourPaymentMethodPageLocators.PAY_BY_BANK)
        el.click()
        return BankWirePaymentPage(self.driver)