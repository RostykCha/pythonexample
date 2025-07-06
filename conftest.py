import json
import os
import pytest
from playwright.sync_api import sync_playwright
from api.client import ApiClient

@pytest.fixture(scope='session')
def cfg():
    env = os.environ.get('ENV', 'qa')
    with open(f'config/{env}.json') as f:
        return json.load(f)

@pytest.fixture(scope='session')
def api(cfg):
    return ApiClient(cfg['api_base'])

@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
