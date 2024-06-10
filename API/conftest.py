import logging

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
    try:
        request = requests.post(url=URL, data=body)
        token = request.json()['token']
    except:
        logging.exception('Exception while request')
        token = None
    logging.info(f'token is {token}')
    return token


@pytest.fixture()
def texttest1():
    return 'This is new post'


@pytest.fixture()
def get_posts_by_title():
    params = {'owner': 'notMe'}
    return send_get_request_with_auth(data['link'], params, 'title')


@pytest.fixture()
def get_posts_by_description():
    params = {'owner': 'Me'}
    return send_get_request_with_auth(data['link'], params, 'description')


@pytest.fixture()
def create_new_post():
    body = {
        'title': data['title'],
        'description': data['description'],
        'content': data['content']
    }
    return send_post_request_with_auth(data['link'], body, 'description')


def send_get_request_with_auth(url, params, mode):
    token = auth()
    if not token:
        logging.error('Not token')
        return None
    try:
        header = {'X-Auth-Token': token}
        res = requests.get(url, headers=header, params=params)
    except:
        logging.exception('Exception while request')
        return None
    lst_res = [i[mode] for i in res.json()['data']]
    logging.info(f'Get response {lst_res}')
    return lst_res


def send_post_request_with_auth(url, body, mode):
    token = auth()
    if not token:
        logging.error('Not token')
        return None
    try:
        header = {'X-Auth-Token': token}
        res = requests.post(url, headers=header, data=body)
    except:
        logging.exception('Exception while request')
        return None
    lst_res = res.json()[mode]
    logging.info(f'Get response {lst_res}')
    return lst_res
