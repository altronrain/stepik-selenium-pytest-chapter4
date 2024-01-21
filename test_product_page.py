from pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_alert_with_product_name_after_adding_to_cart()
    page.check_product_name_after_cart_adding()
    page.should_be_alert_with_product_price_after_adding_to_cart()
    page.check_alert_cart_price_after_cart_adding()
    