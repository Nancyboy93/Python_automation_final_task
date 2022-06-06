from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from time import sleep
import pytest

@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        self.page = LoginPage(browser, self.link)
        self.page.open()
        self.page.register_new_user()
        self.page.should_be_authorized_user

    def test_user_can_add_to_basket(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, self.link)
        page.open()
        page.should_see_button()
        page.add_to_basket()
        page.should_be_adding_book_message()
        page.should_be_adding_price_message()
        page.should_match()

    def test_user_cant_see_success_message(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, self.link)
        page.open()
        page.guest_cant_see_success_message()


@pytest.mark.xfail
def test_user_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.guest_cant_see_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
def test_guest_can_go_to_login_page_from_product_page(browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.check_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.guest_cant_see_products_in_basket()
    basket_page.guest_can_see_message_about_empty_basket()




