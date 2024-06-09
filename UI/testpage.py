from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    LOCATOR_PASS_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    LOCATOR_TITLE_INPUT_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    LOCATOR_DESCRIPTION_INPUT_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea')
    LOCATOR_CONTENT_INPUT_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea')
    LOCATOR_LOGIN_BTN_CSS = (By.CSS_SELECTOR, 'button')
    LOCATOR_ERROR_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')
    LOCATOR_DIV_LOGIN_FIELD = (By.CSS_SELECTOR, "span.mdc-text-field__ripple")
    LOCATOR_LOGIN_BTN_XPATH = (By.XPATH, '//*[@id="login"]/div[3]/button/div')
    LOCATOR_SAVE_POST_BTN = (By.CLASS_NAME, 'mdc-button__ripple')
    LOCATOR_HELLO_USER = (By.XPATH, '/html/body/div[1]/main/nav/ul/li[3]/a')
    LOCATOR_TITLE_OF_POST = By.XPATH, '//*[@id="app"]/main/div/div[1]/h1'
    LOCATOR_PLUS_BTN = By.ID, 'create-btn'


class OperationHelper(BasePage):
    def enter_login(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN_CSS).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f'We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def get_login_div_height(self):
        return self.get_element_properties(TestSearchLocators.LOCATOR_DIV_LOGIN_FIELD, 'height')

    def get_login_button_color(self):
        return self.get_element_properties(TestSearchLocators.LOCATOR_LOGIN_BTN_XPATH, 'color')

    def login(self, username, password):
        self.go_to_site()
        self.enter_login(username)
        self.enter_pass(password)
        self.click_login_button()

    def get_hello_text(self):
        return self.find_element(TestSearchLocators.LOCATOR_HELLO_USER).text

    def enter_tittle(self, text):
        login_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_INPUT_FIELD)
        login_field.clear()
        login_field.send_keys(text)

    def enter_description(self, text):
        login_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_INPUT_FIELD)
        login_field.clear()
        login_field.send_keys(text)

    def enter_content(self, text):
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_INPUT_FIELD)
        login_field.clear()
        login_field.send_keys(text)

    def click_save_post_button(self):
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).submit()

    def click_create_post_button_plus(self):
        self.find_element(TestSearchLocators.LOCATOR_PLUS_BTN).click()

    def create_new_post(self, title, description, content):
        self.enter_tittle(title)
        self.enter_description(description)
        self.enter_content(content)
        self.click_save_post_button()

    def get_title_name_post_text(self):
        return self.find_element(TestSearchLocators.LOCATOR_TITLE_OF_POST).text
