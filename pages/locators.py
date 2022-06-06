from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasketLocators():
    BASKET_CONTENT = (By.XPATH, "//div[@class='row']/h2[1]")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//div[@class='content']/div[2]/p")
    BASKET_BUTTON = (By.XPATH, "//span/a")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL_FIELD = (By.XPATH, "//input[@name='registration-email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='registration-password1']")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//input[@name='registration-password2']")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators():
    ADD_BUTTON = (By.XPATH, "//div/form[@id='add_to_basket_form']/button")
    ADDING_BOOK_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div")
    BOOK_NAME = (By.XPATH, "//div/h1")
    ADDED_BOOK_NAME = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    ADDING_PRICE_MESSAGE = (By.XPATH, "//div[@id='messages']/div[3]/div")
    BOOK_PRICE = (By.XPATH, "//article/div/div/p[1]")
    ADDED_BOOK_PRICE = (By.XPATH, "//div[@id='messages']/div[3]/div/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]")


