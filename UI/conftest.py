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
def xpath_selector_btn():
    return '//*[@id="login"]/div[3]/button/div'


@pytest.fixture()
def xpath_selector_hello_user():
    return '/html/body/div[1]/main/nav/ul/li[3]/a'


def login(username_fild_input_selector, password_fild_input_selector, button_selector,
                          page, mode):
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
