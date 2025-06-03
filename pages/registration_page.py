from pages.base_page import BasePage
from locators.page_locators import RegisterPageLocators
from selenium.webdriver.support import expected_conditions as EC
from pages.my_account_page import MyAccountPage
from selenium.webdriver.support.select import Select
from faker import Faker
import random

class RegistrationPage(BasePage):
    """
    Registration Page
    """
    def select_title(self):
        el= self.driver.find_element(*RegisterPageLocators.TITLE_MR)
        el.click()

    def enter_first_name(self):
        el = self.driver.find_element(*RegisterPageLocators.FIRST_NAME)
        el.send_keys(Faker().first_name())

    def enter_last_name(self):
        el = self.driver.find_element(*RegisterPageLocators.LAST_NAME)
        el.send_keys(Faker().last_name())

    def get_displayed_email(self):
        el = self.driver.find_element(*RegisterPageLocators.EMAIL)
        return el.get_attribute("value")

    def enter_password(self):
        el = self.driver.find_element(*RegisterPageLocators.PASSWORD)
        el.send_keys(Faker().password(length=random.randint(5, 10)))

    def enter_date_of_birth(self):
        el_d = self.driver.find_element(*RegisterPageLocators.DAY)
        el_m = self.driver.find_element(*RegisterPageLocators.MONTH)
        el_y = self.driver.find_element(*RegisterPageLocators.YEAR)
        day_select = Select(el_d)
        day_select.select_by_value(str(random.randint(1, 31)))
        month_select = Select(el_m)
        month_select.select_by_value(str(random.randint(1, 12)))
        year_select = Select(el_y)
        year_select.select_by_value(str(random.randint(1990, 2024)))

    def select_newsletter(self):
            el = self.driver.find_element(*RegisterPageLocators.NEWSLETTER)
            el.click()

    def click_register(self):
            el = self.driver.find_element(*RegisterPageLocators.REGISTER)
            el.click()
            self.wait_5s.until(EC.url_contains("my-account"))
            return MyAccountPage(self.driver)

    def click_register_empty_fields(self):
            el = self.driver.find_element(*RegisterPageLocators.REGISTER)
            el.click()
            self.wait_5s.until(EC.visibility_of_element_located(RegisterPageLocators.ALERT_ERROR))

    def get_one_alert(self):
        el= self.driver.find_element(*RegisterPageLocators.ALERT_ERROR)
        assert "There is 1 error" in el.text, \
            f"Oczekiwany komunikat 'There is 1 error', otrzymano: '{el.text}'"

    def get_two_alerts(self):
        el = self.driver.find_element(*RegisterPageLocators.ALERT_ERROR)
        assert "There are 2 errors" in el.text, \
            f"Oczekiwany komunikat 'There are 2 errors', otrzymano: '{el.text}'"

    def get_three_alerts(self):
        el = self.driver.find_element(*RegisterPageLocators.ALERT_ERROR)
        assert "There are 3 errors" in el.text, \
            f"Oczekiwany komunikat 'There are 3 errors', otrzymano: '{el.text}'"

    def get_first_name_alert(self):
        el = self.driver.find_element(*RegisterPageLocators.ALERT_NAME_PASSWORD)
        assert "firstname is required" in el.text, \
            f"Oczekiwany komunikat 'firstname is required', otrzymano: '{el.text}'"

    def get_last_name_alert(self):
        el = self.driver.find_element(*RegisterPageLocators.ALERT_NAME_PASSWORD)
        assert "lastname is required" in el.text, \
            f"Oczekiwany komunikat 'lastname is required', otrzymano: '{el.text}'"

    def get_password_alert(self):
        el = self.driver.find_element(*RegisterPageLocators.ALERT_NAME_PASSWORD)
        assert "passwd is required" in el.text, \
            f"Oczekiwany komunikat 'passwd is required', otrzymano: '{el.text}'"

    def get_fn_ln_alert(self):
        el = self.driver.find_elements(*RegisterPageLocators.ALERTS_NAME_PASSWORD)
        alert_texts = [alert.text for alert in el]
        assert "lastname is required" in "\n".join(alert_texts), \
            f"Oczekiwany jeden z komunikatów 'lastname is required', otrzymano: '{alert_texts}'"
        assert "firstname is required" in "\n".join(alert_texts), \
            f"Oczekiwany jeden z komunikatów 'firstname is required', otrzymano: '{alert_texts}'"

    def get_fn_ln_pd_alert(self):
        el = self.driver.find_elements(*RegisterPageLocators.ALERTS_NAME_PASSWORD)
        alert_texts = [alert.text for alert in el]
        assert "lastname is required" in "\n".join(alert_texts), \
            f"Oczekiwany jeden z komunikatów 'lastname is required', otrzymano: '{alert_texts}'"
        assert "firstname is required" in "\n".join(alert_texts), \
            f"Oczekiwany jeden z komunikatów 'firstname is required', otrzymano: '{alert_texts}'"
        assert "passwd is required" in "\n".join(alert_texts), \
            f"Oczekiwany jeden z komunikatów 'passwd is required', otrzymano: '{alert_texts}'"
