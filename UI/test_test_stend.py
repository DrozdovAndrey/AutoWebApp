from module import Page, testdata
from conftest import login


class TestUI:
    def test_get_property_height_by_css(self, css_selector_field_div_login):
        page = Page(testdata["address"])
        css_selector = css_selector_field_div_login
        height = page.get_element_properties("css", css_selector, 'height')
        assert height == testdata["height"]

    def test_get_property_color_by_xpath(self, xpath_selector_btn):
        page = Page(testdata["address"])
        xpath_selector = xpath_selector_btn
        color = page.get_element_properties("xpath", xpath_selector, 'color')
        assert color == testdata["color"]

    def test_login_failed(self, username_fild_input_selector, password_fild_input_selector, button_selector,
                          error_selector):
        page = Page(testdata["address"])
        login(username_fild_input_selector, password_fild_input_selector, button_selector, page, 'w')
        err_selector = error_selector
        err = page.find_element('xpath', err_selector).text
        page.close()
        assert err == str(testdata["text_err"])

    def test_login_success(self, username_fild_input_selector, password_fild_input_selector, button_selector,
                           xpath_selector_hello_user):
        page = Page(testdata["address"])
        login(username_fild_input_selector, password_fild_input_selector, button_selector, page, 'g')
        hello = page.find_element('xpath',xpath_selector_hello_user).text
        page.close()
        assert hello == testdata["hello"]


