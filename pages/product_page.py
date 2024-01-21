from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
        
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_CART_BUTTON
            ), "'Add to cart' button is not presented"
    

    def add_product_to_cart(self):
        add_to_cart_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

 
    def should_be_alert_with_product_name_after_adding_to_cart(self):
        assert self.is_element_present(
            *ProductPageLocators.ALERT_PRODUCT_NAME
            ), "Message with product name is not presented after adding to cart"
 
    
    def check_product_name_after_cart_adding(self):
        product_name_on_page = self.get_element_text(
            *ProductPageLocators.PRODUCT_NAME)
        alert_product_name = self.get_element_text(
            *ProductPageLocators.ALERT_PRODUCT_NAME)
        assert product_name_on_page == alert_product_name, "Wrong product added to cart!"
        

    def should_be_alert_with_product_price_after_adding_to_cart(self):
        assert self.is_element_present(
            *ProductPageLocators.ALERT_CART_PRICE
            ), "Message with cart price is not presented after adding to cart"
        
    
    def check_alert_cart_price_after_cart_adding(self):
        product_price_on_page = self.get_element_text(
            *ProductPageLocators.PRODUCT_PRICE)
        alert_product_price = self.get_element_text(
            *ProductPageLocators.ALERT_CART_PRICE)
        assert product_price_on_page == alert_product_price, "Wrong cart price!"        
    
    