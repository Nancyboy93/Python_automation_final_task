from pages.product_page import ProductPage
from time import sleep
import pytest

@pytest.mark.parametrize ('endpoint', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4", "?promo=offer5", "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_to_basket(browser, endpoint):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/{endpoint}"
    page = ProductPage(browser, link)
    page.open()
    page.should_see_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_adding_book_message()
    page.should_be_adding_price_message()
    page.should_match()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.guest_cant_see_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.guest_cant_see_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.message_disappeared_after_adding_product_to_basket()


