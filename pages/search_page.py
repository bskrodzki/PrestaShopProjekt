from pages.base_page import BasePage
from locators.page_locators import SearchPageLocators

class SearchPage(BasePage):
    """
    Search Page
    """
    def get_displayed_product(self):
        el = self.driver.find_element(*SearchPageLocators.SEARCH_RESULTS)
        return el.get_attribute("title")