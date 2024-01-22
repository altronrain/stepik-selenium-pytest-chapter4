from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_cart_text(self):
        assert self.get_element_text(
            *BasketPageLocators.EMPTY_CART_TEXT
            ), "Message about empty cart is presented"


    def should_not_be_items_in_cart(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS
            ), "Something is in the cart already!"