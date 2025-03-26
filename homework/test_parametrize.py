"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have


@pytest.fixture(params=[(1920, 1080), (430, 932)])
def setup_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.mark.parametrize("setup_browser", [(1920, 1080)], indirect=True, ids=["1920x1080"])
def test_github_desktop(setup_browser):
    browser.open("https://github.com/")
    browser.all('button').element_by(have.text('Sign up')).click()


@pytest.mark.parametrize("setup_browser", [(430, 932)], indirect=True, ids=["430x932"])
def test_github_mobile(setup_browser):
    browser.open("https://github.com/")
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-up').click()
