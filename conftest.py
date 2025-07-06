import json
import os
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from api.client import APIClient


@pytest.fixture(scope="session")
def cfg():
    env = os.getenv("ENV", "qa")
    cfg_path = Path(__file__).parent / "config" / f"{env}.json"
    with open(cfg_path) as f:
        return json.load(f)


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser, cfg):
    context = browser.new_context(base_url=cfg["base_url"])
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="session")
def api(cfg):
    return APIClient(cfg["api_base_url"])
