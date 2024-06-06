import pytest
import yaml
import requests

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def good_word():
    return 'привет'


@pytest.fixture()
def bad_word():
    return 'правет'


def auth():
    URL = data['login_page']
    body = {
        'username': data['login'],
        'password': data['password']
    }
    request = requests.post(url=URL, data=body)
    return request.json()['token']


@pytest.fixture()
def texttest1():
    return 'tiitle'


@pytest.fixture()
def get_posts_by_title():
    header = {'X-Auth-Token': auth()}
    res = requests.get(data['link'], headers=header, params={'owner': 'notMe'})
    return [i['title'] for i in res.json()['data']]


@pytest.fixture()
def get_posts_by_description():
    header = {'X-Auth-Token': auth()}
    res = requests.get(data['link'], headers=header, params={'owner': 'Me'})
    return [i['description'] for i in res.json()['data']]


@pytest.fixture()
def create_new_post():
    header = {'X-Auth-Token': auth()}
    url = data['link']
    body = {
        'title': data['title'],
        'description': data['description'],
        'content': data['content']
    }
    res = requests.post(url=url, data=body, headers=header)
    return res.json()['description']
