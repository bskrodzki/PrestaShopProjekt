from pages.base_page import BasePage
from pages.authentication_page import AuthenticationPage
from pages.blouses_page import BlousesPage
from pages.search_page import SearchPage
from locators.page_locators import HomePageLocators
from selenium.webdriver import ActionChains


class HomePage(BasePage):
    """
    Home Page
    """
    def click_log_in(self):
        self.driver.find_element(*HomePageLocators.SIGN_IN).click()
        return AuthenticationPage(self.driver)


    def search_product(self, product_name):
        el = self.driver.find_element(*HomePageLocators.SEARCH)
        el.send_keys(product_name)
        return product_name

    def click_search(self):
        self.driver.find_element(*HomePageLocators.SEARCH_BUTTON).click()
        return SearchPage(self.driver)

    def expand_women_menu(self):
        women_menu_element = self.driver.find_element(*HomePageLocators.WOMEN_MENU)
        ActionChains(self.driver).move_to_element(women_menu_element).perform()

    def click_blouses(self):
        self.driver.find_element(*HomePageLocators.BLOUSES).click()
        return BlousesPage(self.driver)
