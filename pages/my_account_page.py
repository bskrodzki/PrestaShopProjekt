from pages.base_page import BasePage
from locators.page_locators import MyAccountPageLocators


class MyAccountPage(BasePage):
    """
    My Account Page
    """
    def get_success_registration_alert(self):
        el= self.driver.find_element(*MyAccountPageLocators.REGISTRATION_SUCCESS)
        assert el.text == "Your account has been created.", \
            f"Oczekiwany komunikat 'Your account has been created.', otrzymano: '{el.text}'"


    def get_customer_account_name(self):
        el = self.driver.find_element(*MyAccountPageLocators.USER_NAME)
        assert el.text == "Jan Kowalski", \
            f"Oczekiwany komunikat 'Jan Kowalski', otrzymano: '{el.text}'"