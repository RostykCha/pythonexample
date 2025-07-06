import pytest


@pytest.mark.api
def test_get_users(api):
    response = api.get("/users")
    assert response.status_code < 500
