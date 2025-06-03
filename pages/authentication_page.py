from pages.base_page import BasePage
from locators.page_locators import AuthenticationPageLocators
from selenium.webdriver.support import expected_conditions as EC
from pages.my_account_page import MyAccountPage
from pages.registration_page import RegistrationPage
from test_data.test_data import AccountDetails
from faker import Faker

class AuthenticationPage(BasePage):
    """
    Authentication Page
    """
    def enter_email(self):
        email = Faker().email()
        el = self.driver.find_element(*AuthenticationPageLocators.EMAIL_INPUT)
        self.wait_5s.until(EC.visibility_of(el))
        el.send_keys(email)
        return email

    def click_create_an_account(self):
        el= self.driver.find_element(*AuthenticationPageLocators.CREATE_AN_ACCOUNT)
        el.click()
        self.wait_5s.until(EC.url_contains("account-creation"))
        return RegistrationPage(self.driver)

    def enter_email_log_in(self):
        email = AccountDetails.email_a
        el = self.driver.find_element(*AuthenticationPageLocators.EMAIL_INPUT2)
        self.wait_5s.until(EC.visibility_of(el))
        el.send_keys(email)

    def enter_password_log_in(self):
        password = AccountDetails.password_a
        el = self.driver.find_element(*AuthenticationPageLocators.PASSWORD_INPUT)
        self.wait_5s.until(EC.visibility_of(el))
        el.send_keys(password)

    def click_sign_in(self):
        el= self.driver.find_element(*AuthenticationPageLocators.SIGN_IN)
        el.click()

    def click_sign_in_correct(self):
        el= self.driver.find_element(*AuthenticationPageLocators.SIGN_IN)
        el.click()
        self.wait_5s.until(EC.url_contains("my-account"))
        return MyAccountPage(self.driver)

    def get_one_alert_sign_in(self):
        el= self.driver.find_element(*AuthenticationPageLocators.ALERT_ERROR)
        assert "There is 1 error" in el.text, \
            f"Oczekiwany komunikat 'There is 1 error', otrzymano: '{el.text}'"

    def get_email_alert(self):
        el = self.driver.find_element(*AuthenticationPageLocators.ALERT_EMAIL_PASSWORD)
        assert "An email address required." in el.text, \
            f"Oczekiwany komunikat 'An email address required.', otrzymano: '{el.text}'"

    def get_password_alert(self):
        el = self.driver.find_element(*AuthenticationPageLocators.ALERT_EMAIL_PASSWORD)
        assert "Password is required." in el.text, \
            f"Oczekiwany komunikat 'Password is required.', otrzymano: '{el.text}'"