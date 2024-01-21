from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner strong")
    ALERT_CART_PRICE = (By.CSS_SELECTOR, "#messages :nth-child(3) .alertinner strong")
    
    
    
    