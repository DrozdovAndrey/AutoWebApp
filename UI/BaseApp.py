import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru/"

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by {locator}")
        except:
            logging.exception("Find element exception")
            element = None
        return element

    def wait_alert(self, time=10):
        return WebDriverWait(self.driver, time).until(EC.alert_is_present())

    def get_element_properties(self, locator, properties):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(properties)
        logging.error(f'Property not found with locator {locator}')

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception('Exception while open page')
            start_browsing = None
        return start_browsing

    def get_alert_text(self):
        try:
            alert = self.wait_alert()
            text = alert.text
            alert.accept()
            logging.info(f'Get text {text} from alert')
            return text
        except:
            logging.exception("Exception with alert")
            return None
