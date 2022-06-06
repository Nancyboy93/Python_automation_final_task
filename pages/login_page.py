from .base_page import BasePage
from .locators import LoginPageLocators
from faker import Faker
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Url doesn't contain login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        email = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email.click()
        f = Faker()
        email.send_keys(f.email())
        password = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password.click()
        password.send_keys(str(time.time))
        password2 = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        password2.click()
        password2.send_keys(str(time.time))
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()


