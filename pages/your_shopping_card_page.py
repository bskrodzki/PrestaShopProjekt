from pages.base_page import BasePage
from pages.addresses_page import AddressesPage
from locators.page_locators import ShoppingCartPageLocators

class YourShoppingCardPage(BasePage):
    """
    Your Shopping Card Page
    """
    def get_unit_price(self):
        unit_price = self.driver.find_element(*ShoppingCartPageLocators.UNIT_PRICE).text
        return unit_price

    def get_total_price(self):
        total_price = self.driver.find_element(*ShoppingCartPageLocators.TOTAL_PRICE).text
        return total_price

    def get_total_products_price(self):
        total_products_price = self.driver.find_element(*ShoppingCartPageLocators.TOTAL_PRODUCTS_PRICE).text
        return total_products_price

    def get_total_shipping_price(self):
        total_shipping_price = self.driver.find_element(*ShoppingCartPageLocators.TOTAL_SHIPPING_PRICE).text
        return total_shipping_price

    def get_total_price_2(self):
        total_price_2 = self.driver.find_element(*ShoppingCartPageLocators.TOTAL_PRICE_2).text
        return total_price_2

    def check_total_amount(self):
        total_products_price_2 = float(self.driver.find_element(*ShoppingCartPageLocators.TOTAL_PRODUCTS_PRICE).text.strip().replace('$', ''))
        total_shipping_price_2 = float(self.driver.find_element(*ShoppingCartPageLocators.TOTAL_SHIPPING_PRICE).text.strip().replace('$', ''))
        #zaokrąglenie do drugiego miejsca po przecinku
        total = round(total_products_price_2 + total_shipping_price_2, 2)
        return total

    def get_total_price_2_float(self):
        total_price_2_float = self.driver.find_element(*ShoppingCartPageLocators.TOTAL_PRICE_2).text.strip().replace('$', '')
        return float(total_price_2_float)

    def click_proceed_to_checkout(self):
        el = self.driver.find_element(*ShoppingCartPageLocators.PROCEED_TO_CHECKOUT)
        el.click()
        return AddressesPage(self.driver)