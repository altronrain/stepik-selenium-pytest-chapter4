from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Link is not for login page"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"


    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_EMAIL)
        reg_email.send_keys(email)
        passwd_box1 = self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_PASSWORD1)
        passwd_box1.send_keys(password)
        passwd_box2 = self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_PASSWORD2)
        passwd_box2.send_keys(password)
        register_button = self.browser.find_element(
            *LoginPageLocators.REGISTER_SUBMIT)
        register_button.click()