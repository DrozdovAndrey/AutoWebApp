from testpage import OperationHelper
import yaml
import time


with open('testdata.yaml') as f:
    data = yaml.safe_load(f)


class TestUI:
    def test_get_property_height_by_css(self, browser):
        page = OperationHelper(browser)
        page.go_to_site()
        height = page.get_login_div_height()
        assert height == data["height"]

    def test_get_property_color_by_xpath(self, browser):
        page = OperationHelper(browser)
        page.go_to_site()
        color = page.get_login_button_color()
        assert color == data["color"]

    def test_login_failed(self, browser):
        page = OperationHelper(browser)
        page.go_to_site_and_login(data["w_username"], data["w_password"])
        text_error = page.get_error_text()
        assert text_error == str(data["text_err"])

    def test_login_success(self, browser):
        page = OperationHelper(browser)
        page.go_to_site_and_login(data["username"], data["password"])
        hello_text = page.get_hello_text()
        assert hello_text == data["hello"]

    def test_create_post(self, browser):
        page = OperationHelper(browser)
        page.go_to_site_and_login(data["username"], data["password"])
        page.click_create_post_button_plus()
        page.create_new_post(data["title"], data["description"], data["content"])
        time.sleep(2)
        name_post = page.get_title_name_post_text()
        assert name_post == data['title']

    def test_user_can_open_contact_us_page(self, browser):
        page = OperationHelper(browser)
        page.go_to_site_and_login(data["username"], data["password"])
        page.click_contact_us()
        time.sleep(2)
        contact_us_text = page.get_contact_us_header_text()
        assert contact_us_text == data["contact_us_header_text"]

    def test_user_can_open_contact_us_page_and_fill_and_confirm_data(self, browser):
        page = OperationHelper(browser)
        page.go_to_site_and_login(data["username"], data["password"])
        page.click_contact_us()
        page.enter_your_name(data["name"])
        page.enter_your_email(data["email"])
        page.enter_contact_content(data["contact_content"])
        page.click_contact_us_button()
        text = page.get_alert_text()
        assert text == data["alert_text"]

