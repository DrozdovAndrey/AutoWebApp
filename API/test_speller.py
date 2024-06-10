from checkers import check_text


class TestSoapApi:
    def test_text_response(self, bad_word, good_word):
        assert good_word in check_text(bad_word)
