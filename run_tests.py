import unittest
import xmlrunner

from tests.basket_tests import BasketTest
from tests.buying_tests import BuyingTest
from tests.create_an_account_tests import CreateAnAccountTest
from tests.log_in_tests import LogInTest
from tests.search_tests import SearchTest

"""
All tests
"""

create_an_account_tests = unittest.TestLoader().loadTestsFromTestCase(CreateAnAccountTest)
log_in_tests = unittest.TestLoader().loadTestsFromTestCase(LogInTest)
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
basket_tests = unittest.TestLoader().loadTestsFromTestCase(BasketTest)
buying_tests = unittest.TestLoader().loadTestsFromTestCase(BuyingTest)

tests_for_run = [
    create_an_account_tests,
    log_in_tests,
    search_tests,
    basket_tests,
    buying_tests
]

test_suite = unittest.TestSuite(tests_for_run)

with open('reports/test-results.xml', 'wb') as output:
    runner = xmlrunner.XMLTestRunner(output=output)
    runner.run(test_suite)