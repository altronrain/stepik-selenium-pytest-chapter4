import math
from .locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException


class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def get_element_text(self, method, element):
        try:
            self.browser.find_element(method, element)
        except (NoSuchElementException):
            return None
        return self.browser.find_element(method, element).text

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def is_disappeared(self, method, element, timeout=4):
        """
        Test will wait for element to disappear from page as long as timeout set
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((method, element)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, method, element):
        try:
            self.browser.find_element(method, element)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, method, element, timeout=4):
        """
        Test will fail immidiately if element (appears) on page during timeout
        """
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((method, element)))
        except TimeoutException:
            return True
        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")