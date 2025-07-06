import pytest

@pytest.mark.api
def test_get_users(api):
    resp = api.get('/users')
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
