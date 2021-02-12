from selenium.webdriver.common.by import By

class HomePageLocators(object):
    PROFILE = (By.CSS_SELECTOR, "div.profile-brief")
    WIDGET_FL = (By.CSS_SELECTOR, "widget-form widget:nth-child(1)")
    WIDGET_IP = (By.CSS_SELECTOR, "widget-form widget:nth-child(2)")
    WIDGET_UL = (By.CSS_SELECTOR, "widget-form widget:nth-child(3)")
    HEADER_WIDGET_FL = (By.CSS_SELECTOR, "widget-form :nth-child(1) .header .title")
    HEADER_WIDGET_IP = (By.CSS_SELECTOR, "widget-form :nth-child(2) .header .title")
    HEADER_WIDGET_UL = (By.CSS_SELECTOR, "widget-form :nth-child(3) .header .title")
    BUTTON_ESC = (By.CSS_SELECTOR, "div.logout")