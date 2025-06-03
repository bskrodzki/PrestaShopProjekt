import time
from tests.base_test import BaseTest

class BuyingTest(BaseTest):
    """
    Buying Tests
    """
    def setUp(self):
        super().setUp()
        self.authentication_page = self.home_page.click_log_in()
        self.authentication_page.enter_email_log_in()
        self.authentication_page.enter_password_log_in()
        self.my_account_page = self.authentication_page.click_sign_in_correct()

    def testOneProductBuying(self):
        self.home_page.expand_women_menu()
        self.blouses_page = self.home_page.click_blouses()
        self.blouse_page = self.blouses_page.click_blouse()
        # nie zawsze pojawia się przycisk add to cart jak za szybko kliknie się kolor
        time.sleep(1)
        self.blouse_page.click_white_color()
        product_price = self.blouse_page.remember_price()
        self.blouse_page.click_add_to_cart()
        # tu sleep tylko po to żeby było widać wyskakujące okienko z komunikatem w przeglądarce
        time.sleep(1)
        self.your_shopping_card_page = self.blouse_page.click_checkout_button()
        unit_price = self.your_shopping_card_page.get_unit_price()
        self.assertEqual(product_price, unit_price)
        total_price = self.your_shopping_card_page.get_total_price()
        self.assertEqual(product_price, total_price)
        total_products_price = self.your_shopping_card_page.get_total_products_price()
        self.assertEqual(product_price, total_products_price)
        total_shipping_price = self.your_shopping_card_page.get_total_shipping_price()
        self.assertEqual("$7", total_shipping_price)
        sum_products_shipping = self.your_shopping_card_page.check_total_amount()
        total_price_2 = self.your_shopping_card_page.get_total_price_2_float()
        self.assertEqual(sum_products_shipping, total_price_2)
        self.addresses_page = self.your_shopping_card_page.click_proceed_to_checkout()
        self.shipping_page = self.addresses_page.click_proceed_to_checkout()
        self.shipping_page.click_terms_agree()
        self.your_payment_method_page = self.shipping_page.click_proceed_to_checkout()
        self.bank_wire_payment_page = self.your_payment_method_page.click_pay_by_bank()
        self.order_confirmation_page = self.bank_wire_payment_page.click_confirm_order()
        self.order_confirmation_page.get_success_alert()