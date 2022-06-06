from .base_page import BasePage
from .locators import BasketLocators

class BasketPage(BasePage):
    def guest_cant_see_products_in_basket(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_CONTENT), \
            "There are products in the basket"

    def guest_can_see_message_about_empty_basket(self):
        assert self.is_element_present(*BasketLocators.EMPTY_BASKET_MESSAGE), "There is no message regarding empty basket"