"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have


@pytest.fixture(params=[(1920, 1080), (430, 932)], ids=["1920x1080", "430x932"])
def setup_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width > 1011:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()


def test_github_desktop(setup_browser):
    if setup_browser == "mobile":
        pytest.skip("Это мобильное разрешение")
    browser.open("https://github.com/")
    browser.all('button').element_by(have.text('Sign up')).click()


def test_github_mobile(setup_browser):
    if setup_browser == "desktop":
        pytest.skip("Это десктопное разрешение")
    browser.open("https://github.com/")
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-up').click()
