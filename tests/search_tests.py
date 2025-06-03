from tests.base_test import BaseTest
from ddt import data, ddt
import csv


def read_csv(file_path):
    """
    Search Tests
    """
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return [row['product_name'] for row in reader]

@ddt
class SearchTest(BaseTest):
    def setUp(self):
        super().setUp()

    @data(*read_csv('test_data/products.csv'))
    def test_search_products(self, product_name):
        entered_product = self.home_page.search_product(product_name)
        self.search_page = self.home_page.click_search()
        displayed_product = self.search_page.get_displayed_product()
        self.assertEqual(entered_product, displayed_product)
