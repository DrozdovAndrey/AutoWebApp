from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by {locator}")

    def wait_alert(self, time=10):
        return WebDriverWait(self.driver, time).until(EC.alert_is_present())

    def get_element_properties(self, locator, properties):
        element = self.find_element(locator)
        return element.value_of_css_property(properties)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_alert_text(self):
        alert = self.wait_alert()
        text = alert.text
        alert.accept()
        return text

