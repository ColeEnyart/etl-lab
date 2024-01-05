import pytest
from client import RequestAPI

@pytest.fixture
def client():
    url = 'https://api.quotable.io/quotes'
    request_api = RequestAPI(url)
    return request_api
    
def test_init_RequestAPI(client):
    assert isinstance(client, object)
    
def test_mass_assignment(client):
    assert client.url == 'https://api.quotable.io/quotes'
    
def test_run_returns_json(client):
    response = client.run()
    assert type(response) == dict
    assert len(response) == 6
    assert set(response.keys()) == {'count', 'totalCount', 'page', 'totalPages', 'lastItemIndex', 'results'}