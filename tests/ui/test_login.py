import pytest
from pages.login_page import LoginPage


@pytest.mark.ui
def test_login(page, cfg):
    login = LoginPage(page)
    login.open()
    # Placeholder assertion
    assert page.url.endswith("/login")
