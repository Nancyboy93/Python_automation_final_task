from pages.product_page import ProductPage
from time import sleep
import pytest

@pytest.mark.parametrize ('endpoint', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4", "?promo=offer5", "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_to_basket(browser, endpoint):
    browser.delete_all_cookies()
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/{endpoint}"
    page = ProductPage(browser, link)
    page.open()
    page.should_see_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    sleep(10000)
    page.should_be_adding_book_message()
    page.should_be_adding_price_message()
    page.should_match()


