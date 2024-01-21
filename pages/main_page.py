from .base_page import BasePage
# from .login_page import LoginPage
from .locators import MainPageLocators


class MainPage(BasePage):
    
    def go_to_login_page(self):
        # Подход с неявным переходом, но явной инициализацией страницы
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # Подход с явным переходом, но неявной инициализацией страницы (добавить)
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        
    
    def should_be_login_link(self):
        # self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        assert self.is_element_present(
            *MainPageLocators.LOGIN_LINK), "Login link is not presented"