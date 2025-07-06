import pytest
from pages.login_page import LoginPage

@pytest.mark.ui
def test_open_login_page(page, cfg):
    login = LoginPage(page, cfg['base_url'])
    login.load()
    assert page.title() != ''
