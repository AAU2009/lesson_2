import pytest
from selene import browser, be, have, by
#проект QA.GURU commit 3
@pytest.fixture()
def configuratio():
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    browser.config.timeout = 10


def test_selene_can_be_found():
    browser.open('https://google.com')
    if browser.element(by.text('Accept all')).matching(be.visible):
        browser.element(by.text('Accept all')).click()

    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()

    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_selene_can_not_be_found():
    browser.open('https://google.com')
    if browser.element(by.text('Accept all')).matching(be.visible):
        browser.element(by.text('Accept all')).click()

    browser.element('[name="q"]').should(be.blank).type('safsafsafafasfsafsafsafsafsafsafsafsaf').press_enter()

    browser.element('[id="result-stats"]').should(have.text('About 0 results'))

