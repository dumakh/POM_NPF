from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

"""This class is the parent of all pages"""
"""it contains all the generic methods and utilites for all the pages"""

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 15).until(EC.title_is(title))
        return self.driver.title


    def is_element_present(self, how, what):
        """find element on the page"""
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    """Будет ждать до тех пор, пока элемент не исчезнет"""
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    """Упадет, как только увидит искомый элемент. Элемент не появился: успех, тест зеленый"""
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    """Ожидание появления определенного текста на элементе на странице"""
    def expected_text_on_element(self, by_locator, text):
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element((by_locator), text))
