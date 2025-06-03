import unittest
from tests.basket_tests import BasketTest
from tests.buying_tests import BuyingTest
from tests.create_an_account_tests import CreateAnAccountTest
from tests.log_in_tests import LogInTest
from tests.search_tests import SearchTest
import HtmlTestRunner

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

runner = HtmlTestRunner.HTMLTestRunner(
    output='reports',
    report_name='TestReport',
    combine_reports=True,
    add_timestamp=True
)

runner.run(test_suite)