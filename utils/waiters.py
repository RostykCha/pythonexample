from playwright.sync_api import Page


def wait_for_selector(page: Page, selector: str, timeout: int = 5000):
    """Wait for a selector to be visible."""
    page.wait_for_selector(selector, state="visible", timeout=timeout)
