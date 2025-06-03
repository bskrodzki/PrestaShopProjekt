from tests.base_test import BaseTest
import time

class CreateAnAccountTest(BaseTest):
    """
    Create An Account Tests
    """
    def setUp(self):
        super().setUp()
        self.authentication_page = self.home_page.click_log_in()


    def testCorrectRegistration(self):
         entered_email = self.authentication_page.enter_email()
         self.registration_page = self.authentication_page.click_create_an_account()
         self.registration_page.select_title()
         self.registration_page.enter_first_name()
         self.registration_page.enter_last_name()
         displayed_email = self.registration_page.get_displayed_email()
         self.assertEqual(entered_email, displayed_email)
         self.registration_page.enter_password()
         self.registration_page.enter_date_of_birth()
         self.registration_page.select_newsletter()
         self.my_account_page = self.registration_page.click_register()
         time.sleep(3)
         self.my_account_page.get_success_registration_alert()

    def testCorrectRegistrationWithoutOpt(self):
        entered_email = self.authentication_page.enter_email()
        self.registration_page = self.authentication_page.click_create_an_account()
        self.registration_page.enter_first_name()
        self.registration_page.enter_last_name()
        displayed_email = self.registration_page.get_displayed_email()
        self.assertEqual(entered_email, displayed_email)
        self.registration_page.enter_password()
        self.my_account_page = self.registration_page.click_register()
        time.sleep(3)
        self.my_account_page.get_success_registration_alert()

    def testIncorrectRegistrationWithoutFN(self):
        entered_email = self.authentication_page.enter_email()
        self.registration_page = self.authentication_page.click_create_an_account()
        self.registration_page.select_title()
        self.registration_page.enter_last_name()
        displayed_email = self.registration_page.get_displayed_email()
        self.assertEqual(entered_email, displayed_email)
        self.registration_page.enter_password()
        self.registration_page.enter_date_of_birth()
        self.registration_page.select_newsletter()
        self.registration_page.click_register_empty_fields()
        self.registration_page.get_one_alert()
        self.registration_page.get_first_name_alert()

    def testIncorrectRegistrationWithoutLN(self):
        entered_email = self.authentication_page.enter_email()
        self.registration_page = self.authentication_page.click_create_an_account()
        self.registration_page.select_title()
        self.registration_page.enter_first_name()
        displayed_email = self.registration_page.get_displayed_email()
        self.assertEqual(entered_email, displayed_email)
        self.registration_page.enter_password()
        self.registration_page.enter_date_of_birth()
        self.registration_page.select_newsletter()
        self.registration_page.click_register_empty_fields()
        self.registration_page.get_one_alert()
        self.registration_page.get_last_name_alert()

    def testIncorrectRegistrationWithoutPassword(self):
        entered_email = self.authentication_page.enter_email()
        self.registration_page = self.authentication_page.click_create_an_account()
        self.registration_page.select_title()
        self.registration_page.enter_first_name()
        self.registration_page.enter_last_name()
        displayed_email = self.registration_page.get_displayed_email()
        self.assertEqual(entered_email, displayed_email)
        self.registration_page.enter_date_of_birth()
        self.registration_page.select_newsletter()
        self.registration_page.click_register_empty_fields()
        self.registration_page.get_one_alert()
        self.registration_page.get_password_alert()

    def testIncorrectRegistrationWithoutFNLN(self):
        entered_email = self.authentication_page.enter_email()
        self.registration_page = self.authentication_page.click_create_an_account()
        self.registration_page.select_title()
        displayed_email = self.registration_page.get_displayed_email()
        self.assertEqual(entered_email, displayed_email)
        self.registration_page.enter_password()
        self.registration_page.enter_date_of_birth()
        self.registration_page.select_newsletter()
        self.registration_page.click_register_empty_fields()
        self.registration_page.get_two_alerts()
        self.registration_page.get_fn_ln_alert()

    def testIncorrectRegistrationWithoutFNLNPD(self):
        entered_email = self.authentication_page.enter_email()
        self.registration_page = self.authentication_page.click_create_an_account()
        self.registration_page.select_title()
        displayed_email = self.registration_page.get_displayed_email()
        self.assertEqual(entered_email, displayed_email)
        self.registration_page.enter_date_of_birth()
        self.registration_page.select_newsletter()
        self.registration_page.click_register_empty_fields()
        self.registration_page.get_three_alerts()
        self.registration_page.get_fn_ln_pd_alert()


