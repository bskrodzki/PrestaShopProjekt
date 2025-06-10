import time
from tests.base_test import BaseTest

class BasketTest(BaseTest):
    """
    Basket Tests
    """
    def setUp(self):
        super().setUp()

    def testOneProductInBasket(self):
        self.home_page.expand_women_menu()
        self.blouses_page = self.home_page.click_blouses()
        self.blouse_page = self.blouses_page.click_blouse()
        # nie zawsze pojawia się przycisk add to cart jak za szybko kliknie się kolor
        time.sleep(1)
        self.blouse_page.click_white_color()
        product_price = self.blouse_page.remember_price_float()
        self.blouse_page.click_add_to_cart()
        self.blouse_page.get_one_item()
        total_products_price = self.blouse_page.get_total_products_price()
        self.assertEqual(product_price, total_products_price)
        shipping_price = self.blouse_page.get_shipping_price()
        self.assertEqual(float(7), shipping_price)
        sum_products_shipping = self.blouse_page.check_total_price()
        total_price_2 = self.blouse_page.get_total_price_2()
        self.assertEqual(sum_products_shipping, total_price_2)

    def testTwoProductInBasket(self):
        self.home_page.expand_women_menu()
        self.blouses_page = self.home_page.click_blouses()
        self.blouse_page = self.blouses_page.click_blouse()
        # nie zawsze pojawia się przycisk add to cart jak za szybko kliknie się kolor
        time.sleep(1)
        self.blouse_page.click_white_color()
        product_price = self.blouse_page.remember_price_float()
        self.blouse_page.click_plus_icon()
        self.blouse_page.click_add_to_cart()
        self.blouse_page.get_two_items()
        total_products_price = self.blouse_page.get_total_products_price()
        self.assertEqual(product_price*2, total_products_price)
        shipping_price = self.blouse_page.get_shipping_price()
        self.assertEqual(float(7), shipping_price)
        sum_products_shipping = self.blouse_page.check_total_price()
        total_price_2 = self.blouse_page.get_total_price_2()
        self.assertEqual(sum_products_shipping, total_price_2)
