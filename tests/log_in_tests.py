from tests.base_test import BaseTest

class LogInTest(BaseTest):
    """
    Log In Tests
    """
    def setUp(self):
        super().setUp()
        self.authentication_page = self.home_page.click_log_in()

    def testIncorrectSignInWithoutPassword(self):
        self.authentication_page.enter_email_log_in()
        self.authentication_page.click_sign_in()
        self.authentication_page.get_one_alert_sign_in()
        self.authentication_page.get_password_alert()

    def testIncorrectSignInWithoutEmail(self):
        self.authentication_page.enter_password_log_in()
        self.authentication_page.click_sign_in()
        self.authentication_page.get_one_alert_sign_in()
        self.authentication_page.get_email_alert()

    def testCorrectSignIn(self):
        self.authentication_page.enter_email_log_in()
        self.authentication_page.enter_password_log_in()
        self.my_account_page = self.authentication_page.click_sign_in_correct()
        self.my_account_page.get_customer_account_name()
