import pytest


def test_status_code(get_request):
    assert get_request.status_code == 200


def test_content_type_json(get_request):
    assert get_request.headers['content-type'] == "application/json"


@pytest.mark.parametrize('breed_of_dogs', ['affenpinscher', 'borzoi', 'akita', 'drathar'])
def test_response_json(breed_of_dogs, get_request):
    response_json = get_request.json()
    assert breed_of_dogs in response_json['message']
