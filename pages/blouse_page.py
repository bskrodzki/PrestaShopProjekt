from pages.base_page import BasePage
from locators.page_locators import BlousePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.your_shopping_card_page import YourShoppingCardPage


class BlousePage(BasePage):
    """
    Blouse Page
    """
    def click_white_color(self):
        self.driver.find_element(*BlousePageLocators.WHITE_COLOR).click()

    def click_add_to_cart(self):
        self.driver.find_element(*BlousePageLocators.ADD_TO_CART).click()

    def get_one_item(self):
        el = self.driver.find_element(*BlousePageLocators.QUANTITY_INFORMATION)
        assert "There is 1 item in your cart." in el.text, \
            f"Oczekiwany komunikat 'There is 1 item in your cart.', otrzymano: '{el.text}'"

    def click_plus_icon(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(BlousePageLocators.PLUS_ICON))
        element.click()

    def get_two_items(self):
        el = self.driver.find_element(*BlousePageLocators.QUANTITY_INFORMATION_2)
        assert "2" in el.text, \
            f"Oczekiwana ilość produktów '2', otrzymano: '{el.text}'"

    def click_checkout_button(self):
        self.driver.find_element(*BlousePageLocators.PROCEED_TO_CHECKOUT).click()
        return YourShoppingCardPage(self.driver)

    def remember_price(self):
        price = self.driver.find_element(*BlousePageLocators.PRICE).text
        return price

    def remember_price_float(self):
        price_float = self.driver.find_element(*BlousePageLocators.PRICE).text.strip().replace('$', '')
        return float(price_float)

    def get_total_products_price(self):
        total_products_price = self.driver.find_element(*BlousePageLocators.TOTAL_PRODUCTS_PRICE).text.strip().replace('$', '')
        return float(total_products_price)

    def get_shipping_price(self):
        shipping_price = self.driver.find_element(*BlousePageLocators.SHIPPING_PRICE).text.strip().replace('$', '')
        return float(shipping_price)

    def check_total_price(self):
        total_products_price = float(self.driver.find_element(*BlousePageLocators.TOTAL_PRODUCTS_PRICE).text.strip().replace('$', ''))
        shipping_price = float(self.driver.find_element(*BlousePageLocators.SHIPPING_PRICE).text.strip().replace('$', ''))
        #zaokrąglenie do drugiego miejsca po przecinku
        total = round(total_products_price +  shipping_price, 2)
        return total

    def get_total_price_2(self):
        total_price_2 = self.driver.find_element(*BlousePageLocators.TOTAL_PRICE_2).text.strip().replace('$', '')
        return float(total_price_2)