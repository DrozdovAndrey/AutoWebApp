from module import Page, testdata
from conftest import login, create_post


class TestUI:
    def test_get_property_height_by_css(self, css_selector_field_div_login):
        page = Page(testdata["address"])
        height = page.get_element_properties("css", css_selector_field_div_login, 'height')
        assert height == testdata["height"]

    def test_get_property_color_by_xpath(self, xpath_selector_login_btn):
        page = Page(testdata["address"])
        color = page.get_element_properties("xpath", xpath_selector_login_btn, 'color')
        assert color == testdata["color"]

    def test_login_failed(self, username_fild_input_selector, password_fild_input_selector, button_selector,
                          error_selector):
        page = Page(testdata["address"])
        login(username_fild_input_selector, password_fild_input_selector, button_selector, page, 'w')
        err = page.find_element('xpath', error_selector).text
        page.close()
        assert err == str(testdata["text_err"])

    def test_login_success(self, username_fild_input_selector, password_fild_input_selector, button_selector,
                           xpath_selector_hello_user):
        page = Page(testdata["address"])
        login(username_fild_input_selector, password_fild_input_selector, button_selector, page, 'g')
        hello = page.find_element('xpath', xpath_selector_hello_user).text
        page.close()
        assert hello == testdata["hello"]

    def test_create_post(self, username_fild_input_selector, password_fild_input_selector, button_selector,
                         id_selector_plus, title_field_input_selector, description_field_input_selector,
                         content_field_input_selector, xpath_selector_name_post, class_selector_save_btn):
        page = Page(testdata["address"])
        login(username_fild_input_selector, password_fild_input_selector, button_selector, page, 'g')
        create_post(class_selector_save_btn, page,
                    id_selector_plus, title_field_input_selector, description_field_input_selector,
                    content_field_input_selector)
        name_post = page.find_element("xpath", xpath_selector_name_post).text
        page.close()
        assert name_post == testdata['title']
