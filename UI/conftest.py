
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import pytest
import yaml

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture(scope="session")
def browser():
    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.close()

#
#
#
# def create_post(class_selector_save_btn, page,
#                 id_selector_plus, title_field_input_selector, description_field_input_selector,
#                 content_field_input_selector):
#     time.sleep(5)
#     plus = page.find_element('id', id_selector_plus)
#     plus.click()
#     time.sleep(5)
#     title = page.find_element("xpath", title_field_input_selector)
#     description = page.find_element("xpath", description_field_input_selector)
#     content = page.find_element("xpath", content_field_input_selector)
#     title.send_keys(testdata["title"])
#     description.send_keys(testdata["description"])
#     content.send_keys(testdata["content"])
#     time.sleep(5)
#     btn = page.find_element('class', class_selector_save_btn)
#     btn.submit()
#     time.sleep(5)
