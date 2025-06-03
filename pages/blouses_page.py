from pages.base_page import BasePage
from locators.page_locators import BlousesPageLocators
from pages.blouse_page import BlousePage

class BlousesPage(BasePage):
    """
    Blouses Page
    """
    def click_blouse(self):
        self.driver.find_element(*BlousesPageLocators.BLOUSE).click()
        return BlousePage(self.driver)