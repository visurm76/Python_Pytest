import requests
import pytest
import utils as u

link = u.url['dog']


@pytest.fixture(scope="session")
def get_request():
    r = requests.get(link)
    return r
