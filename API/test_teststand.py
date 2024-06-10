import requests
import yaml


with open('config.yaml') as f:
    data = yaml.safe_load(f)


class TestRestApi:
    def test_step1(self, get_posts_by_title, texttest1):
        assert texttest1 in get_posts_by_title

    def test_step2(self, create_new_post, get_posts_by_description):
        assert create_new_post in get_posts_by_description
