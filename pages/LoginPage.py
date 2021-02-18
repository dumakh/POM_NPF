from pages.BasePage import BasePage
from config.config import TestData
from locators.LoginLocators import LoginPageLocators
from pages.WidgetPage import WidgetPage
class LoginPage(BasePage):

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """page actions for login page"""

    """this is used to get the page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """this is used to chek header"""
    def is_signup_header_exist(self):
        return self.is_visible(LoginPageLocators.SIGNUP_HEADER)

    """this is used to login in to app"""
    def do_login(self, username, password):
        self.do_send_keys(LoginPageLocators.USERNAME, username)
        self.do_send_keys(LoginPageLocators.PASSWORD, password)
        self.do_click(LoginPageLocators.LOGIN_BUTTON)
        return WidgetPage(self.driver)
