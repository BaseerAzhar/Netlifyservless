import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.test_case_1
def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://example.com')
        assert page.title() == 'Example Domain'
        browser.close()
