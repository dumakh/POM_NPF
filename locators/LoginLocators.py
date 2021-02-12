from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    USERNAME = (By.CSS_SELECTOR, '[tabindex="1"]')
    PASSWORD = (By.CSS_SELECTOR, '[tabindex="2"]')
    LOGIN_BUTTON = (By.ID, "kc-login")
    SIGNUP_HEADER = (By.CSS_SELECTOR, ".login-pf-header")