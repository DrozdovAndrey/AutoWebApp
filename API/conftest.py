import pytest


@pytest.fixture()
def lat():
    return 37.7891838


@pytest.fixture()
def long():
    return -122.4033522


@pytest.fixture()
def radius():
    return 1000


@pytest.fixture()
def text():
    return 'One Montgomery Tower'
