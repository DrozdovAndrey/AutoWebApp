import time

import pytest
import yaml

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def username_fild_input_selector():
    return '//*[@id="login"]/div[1]/label/input'


@pytest.fixture()
def password_fild_input_selector():
    return '//*[@id="login"]/div[2]/label/input'


@pytest.fixture()
def title_field_input_selector():
    return '//*[@id="create-item"]/div/div/div[1]/div/label/input'


@pytest.fixture()
def description_field_input_selector():
    return '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'


@pytest.fixture()
def content_field_input_selector():
    return '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'


@pytest.fixture()
def button_selector():
    return 'button'


@pytest.fixture()
def error_selector():
    return '//*[@id="app"]/main/div/div/div[2]/h2'


@pytest.fixture()
def bad_username_password():
    return testdata["w_username"], testdata["w_password"]


@pytest.fixture()
def css_selector_field_div_login():
    return "span.mdc-text-field__ripple"


@pytest.fixture()
def xpath_selector_login_btn():
    return '//*[@id="login"]/div[3]/button/div'


@pytest.fixture()
def class_selector_save_btn():
    return 'mdc-button__ripple'


@pytest.fixture()
def xpath_selector_hello_user():
    return '/html/body/div[1]/main/nav/ul/li[3]/a'


@pytest.fixture()
def xpath_selector_name_post():
    return '//*[@id="app"]/main/div/div[1]/h1'


@pytest.fixture()
def id_selector_plus():
    return 'create-btn'


def login(username_fild_input_selector, password_fild_input_selector, button_selector, page, mode):
    page_ = page
    username_selector = username_fild_input_selector
    username = page_.find_element('xpath', username_selector)
    password_selector = password_fild_input_selector
    password = page_.find_element('xpath', password_selector)
    if mode == 'w':
        username.send_keys(testdata['w_username'])
        password.send_keys(testdata['w_password'])
    elif mode == 'g':
        username.send_keys(testdata['username'])
        password.send_keys(testdata['password'])
    btn_selector = button_selector
    btn = page_.find_element('css', btn_selector)
    btn.click()


def create_post(class_selector_save_btn, page,
                id_selector_plus, title_field_input_selector, description_field_input_selector,
                content_field_input_selector):
    time.sleep(5)
    plus = page.find_element('id', id_selector_plus)
    plus.click()
    time.sleep(5)
    title = page.find_element("xpath", title_field_input_selector)
    description = page.find_element("xpath", description_field_input_selector)
    content = page.find_element("xpath", content_field_input_selector)
    title.send_keys(testdata["title"])
    description.send_keys(testdata["description"])
    content.send_keys(testdata["content"])
    time.sleep(5)
    btn = page.find_element('class', class_selector_save_btn)
    btn.submit()
    time.sleep(5)
