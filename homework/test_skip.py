"""
Параметризуйте фикстуру несколькими вариантами размеров окна.
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
import selene


@pytest.fixture(params=[
    {'width': 414, 'height': 896}, {'width': 3840, 'height': 2160}, {'width': 390, 'height': 844}])
def browser(request):
    browser = selene.browser
    browser.config.window_width = request.param['width']
    browser.config.window_height = request.param['height']
    return browser, request.param


@pytest.fixture()
def is_mobile(request):
    if request.getfixturevalue('browser')[1]['width'] < 1010:
        return True


def test_github_desktop(browser, is_mobile):
    if is_mobile:
        pytest.skip(reason="Это разрешение для мобилки")
    main_page = browser[0].open("https://github.com")
    main_page.element('[href="/login"]').click()


def test_github_mobile(browser, is_mobile):
    if not is_mobile:
        pytest.skip(reason="Это разрешение для десктопа")
    main_page = browser[0].open("https://github.com")
    main_page.element('[class="flex-1 flex-order-2 text-right"] [aria-label="Toggle navigation"]').click()
    main_page.element('[href="/login"]').click()
