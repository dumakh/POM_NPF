from tests.test_base import BaseTest
from pages.LoginPage import LoginPage
from config.config import TestData


class TestWidget(BaseTest):

    def test_widget_page_title(self):
        self.loginPage = LoginPage(self.driver)
        widgetPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = widgetPage.get_home_page_title(TestData.WIDGET_PAGE_TITLE)
        assert title == TestData.WIDGET_PAGE_TITLE

    def test_widget_fl_header(self):
        self.loginPage = LoginPage(self.driver)
        widgetPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        fl_header = widgetPage.get_widget_fl_header()
        assert fl_header == TestData.FL_HEADER

    def test_widget_ip_header(self):
        self.loginPage = LoginPage(self.driver)
        widgetPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        ip_header = widgetPage.get_widget_ip_header()
        assert ip_header == TestData.IP_HEADER

    def test_widget_ul_header(self):
        self.loginPage = LoginPage(self.driver)
        widgetPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        ul_header = widgetPage.get_widget_ul_header()
        assert ul_header == TestData.UL_HEADER

    def test_logout_button(self):
        self.loginPage = LoginPage(self.driver)
        widgetPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        widgetPage.button_logout()
