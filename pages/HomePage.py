#from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from locators.Home_locators import HomePageLocators

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def get_widget_fl_header(self):
        if self.is_visible(HomePageLocators.WIDGET_FL):
            return self.get_element_text(HomePageLocators.HEADER_WIDGET_FL)

    def get_widget_ip_header(self):
        if self.is_visible(HomePageLocators.WIDGET_IP):
            return self.get_element_text(HomePageLocators.HEADER_WIDGET_IP)

    def get_widget_ul_header(self):
        if self.is_visible(HomePageLocators.WIDGET_UL):
            return self.get_element_text(HomePageLocators.HEADER_WIDGET_UL)

    def button_logout(self):
        self.do_click(HomePageLocators.BUTTON_ESC)