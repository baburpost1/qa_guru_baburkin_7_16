import pytest
from selene import browser

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


@pytest.fixture(params=['height', 'width'])
def set_desktop_size(request):
    browser.config.window_height = pytest.param('height')
    browser.config.window_width = pytest.param('width')

@pytest.fixture()
def set_mobile_size():
    browser.config.window_height = 896
    browser.config.window_width = 414

@pytest.mark.parametrize("set_desktop_size", [(2160, 3840), (1111, 356)], indirect=True)
def test_github_desktop(set_desktop_size):
    main_page = browser.open("https://github.com")
    main_page.element('[href="/login"]').click()


def test_github_mobile(set_mobile_size):
    main_page = browser.open("https://github.com")
    main_page.element('[class="flex-1 flex-order-2 text-right"] [aria-label="Toggle navigation"]').click()
    main_page.element('[href="/login"]').click()