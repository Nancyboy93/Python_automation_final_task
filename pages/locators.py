from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_BUTTON = (By.XPATH, "//div/form[@id='add_to_basket_form']/button")
    ADDING_BOOK_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div")
    BOOK_NAME = (By.XPATH, "//div/h1")
    ADDED_BOOK_NAME = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    ADDING_PRICE_MESSAGE = (By.XPATH, "//div[@id='messages']/div[3]/div")
    BOOK_PRICE = (By.XPATH, "//article/div/div/p[1]")
    ADDED_BOOK_PRICE = (By.XPATH, "//div[@id='messages']/div[3]/div/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]")


