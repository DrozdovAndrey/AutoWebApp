from BaseApp import BasePage
from test_page_locators import TestSearchLocators
import logging


class OperationHelper(BasePage):
    # enter
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_LOGIN_FIELD, word, 'login field')

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_PASS_FIELD, word, 'pass field')

    def enter_tittle(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_TITLE_INPUT_FIELD, word)

    def enter_description(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_DESCRIPTION_INPUT_FIELD, word)

    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_CONTENT_INPUT_FIELD, word)

    def enter_your_name(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_YOUR_NAME_FIELD, word)

    def enter_your_email(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_YOUR_EMAIL_FIELD, word)

    def enter_contact_content(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD, word)

    # click
    def click_login_button(self):
        self.click_btn(TestSearchLocators.LOCATOR_LOGIN_BTN_CSS)

    def click_save_post_button(self):
        self.submit_btn(TestSearchLocators.LOCATOR_SAVE_POST_BTN)

    def click_create_post_button_plus(self):
        self.click_btn(TestSearchLocators.LOCATOR_PLUS_BTN)

    def click_contact_us(self):
        self.click_btn(TestSearchLocators.LOCATOR_CONTACT_US)

    def click_contact_us_button(self):
        self.submit_btn(TestSearchLocators.LOCATOR_CONTACT_US_BTN)

    #     get
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.LOCATOR_ERROR_FIELD)

    def get_login_div_height(self):
        return self.get_element_properties(TestSearchLocators.LOCATOR_DIV_LOGIN_FIELD, 'height')

    def get_login_button_color(self):
        return self.get_element_properties(TestSearchLocators.LOCATOR_LOGIN_BTN_XPATH, 'color')

    def get_hello_text(self):
        return self.get_text_from_element(TestSearchLocators.LOCATOR_HELLO_USER)

    def get_title_name_post_text(self):
        return self.get_text_from_element(TestSearchLocators.LOCATOR_TITLE_OF_POST)

    def get_contact_us_header_text(self):
        return self.get_text_from_element(TestSearchLocators.LOCATOR_CONTACT_US_HEADER)

    # group logic
    def create_new_post(self, title, description, content):
        self.enter_tittle(title)
        self.enter_description(description)
        self.enter_content(content)
        self.click_save_post_button()

    def go_to_site_and_login(self, username, password):
        self.go_to_site()
        self.login(username, password)

    def login(self, username, password):
        self.go_to_site()
        self.enter_login(username)
        self.enter_pass(password)
        self.click_login_button()

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.info(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {element_name} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with element {element_name}")
            return False
        return True

    def click_btn(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        btn = self.find_element(locator)
        if not btn:
            return False
        try:
            btn.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.info(f"Click button {element_name}")
        return True

    def submit_btn(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        btn = self.find_element(locator)
        if not btn:
            return False
        try:
            btn.submit()
        except:
            logging.exception("Exception with click")
            return False
        logging.info(f"Submit button {element_name}")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            logging.error(f'Element {element_name} not found')
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from element {element_name}")
            return None
        logging.info(f'We find text {text} in field {element_name}')
        return text
