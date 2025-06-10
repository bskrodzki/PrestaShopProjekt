import unittest
from selenium import webdriver
from pages.home_page import HomePage

class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://automationpractice.pl/")
        self.home_page = HomePage(self.driver)
        # self.driver.implicitly_wait(3000)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()