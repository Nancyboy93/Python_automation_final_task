from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_see_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add to the basket button is not presented"

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_be_adding_book_message(self):
        adding_book_message = self.browser.find_element(*ProductPageLocators.ADDING_BOOK_MESSAGE).text
        assert adding_book_message == "Coders at Work has been added to your basket.", \
            f"Got {adding_book_message} instead of expected"

    def should_be_adding_price_message(self):
        assert self.is_element_present(*ProductPageLocators.ADDING_PRICE_MESSAGE), "There is no message regarding basket value"

    def should_match(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        added_book_name = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_NAME).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        added_book_price = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_PRICE).text
        assert book_name == added_book_name, "Book name doesn't match"
        assert book_price == added_book_price, "Book price doesn't match"

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message isn't disappeared"



