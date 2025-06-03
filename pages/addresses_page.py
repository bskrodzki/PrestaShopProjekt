from pages.base_page import BasePage
from locators.page_locators import AddressesPageLocators
from pages.shipping_page import ShippingPage


class AddressesPage(BasePage):
    """
    Addresses Page
    """
    def click_proceed_to_checkout(self):
        el = self.driver.find_element(*AddressesPageLocators.PROCEED_TO_CHECKOUT)
        el.click()
        return ShippingPage(self.driver)