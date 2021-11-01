from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_to_basket(self):
        busket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        busket_button.click()
        self.solve_quiz_and_get_code()

    def book_name_presented_in_add_msg(self):
        book_in_shop_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_MSG).text
        book_in_basket_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_SHOP).text
        assert book_in_shop_name == book_in_basket_name, "Book names not match"

    def price_is_match(self):
        price_in_shop = self.browser.find_element(*ProductPageLocators.PRICE_IN_SHOP).text
        price_in_msg = self.browser.find_element(*ProductPageLocators.PRICE_IN_MSG).text
        assert price_in_shop == price_in_msg, "Price is not match"

    def promo_is_possible(self):
        promo_msg = self.browser.find_element(*ProductPageLocators.PROMO_MSG).text
        assert promo_msg == "Coders at Work", "Promo is not possible"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared (self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"