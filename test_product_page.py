from pages.product_page import ProductPage
import pytest
import time


class TestUserAddToBasketFromProductPage():
    @pytest.mark.skip
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.price_is_match()
        time.sleep(30)
        page.book_name_presented_in_add_msg()

    @pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6",
                                             pytest.param("7", marks=pytest.mark.xfail(
                                                 reason="bug on page, which will not be fixed")),
                                             "8", "9"])
    # autotest for finding a page with a bug when adding a product
    @pytest.mark.skip
    def test_guest_can_correct_add_promo_product_to_basket(self, browser, promo_offer):
        link = f"http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        time.sleep(1)
        page.promo_is_possible()

    @pytest.mark.xfail(reason="expected falling test")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    @pytest.mark.skip
    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="expected falling test")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.is_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        #time.sleep(60)
        page.go_to_login_page()