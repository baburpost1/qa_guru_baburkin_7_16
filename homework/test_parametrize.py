"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
import selene
from selene import browser


# selene.browser.config.timeout = 4


@pytest.fixture(params=[{"height": 3860, "width": 2180}])
def browser(request):
    browser = selene.browser
    browser.config.window_height = request.param['height']
    browser.config.window_width = request.param['width']
    return browser


@pytest.mark.parametrize('browser', [{"height": 1000, "width": 2000}, {"height": 1000, "width": 1600}], indirect=True)
def test_github_desktop(browser):
    main_page = browser.open("https://github.com")
    main_page.element('[href="/login"]').click()

@pytest.mark.parametrize('browser', [{"height": 1000, "width": 1000},{"height": 896, "width": 414}], indirect=True)
def test_github_mobile(browser):
    main_page = browser.open("https://github.com")
    main_page.element('[class="flex-1 flex-order-2 text-right"] [aria-label="Toggle navigation"]').click()
    main_page.element('[href="/login"]').click()
