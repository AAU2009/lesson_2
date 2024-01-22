import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def configuration():
    browser.config.window_height = 270
    browser.config.window_width = 180
    browser.config.timeout = 10
