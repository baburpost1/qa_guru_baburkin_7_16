import pytest
from selene import browser, Browser

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


@pytest.fixture()
def set_desktop_size():
    browser.config.window_height = 2160
    browser.config.window_width = 3840


@pytest.fixture()
def set_mobile_size():
    browser.config.window_height = 896
    browser.config.window_width = 414


def test_github_desktop(set_desktop_size):
    main_page = browser.open("https://github.com")
    main_page.element('[href="/login"]').click()


def test_github_mobile(set_mobile_size):
    main_page = browser.open("https://github.com")
    main_page.element('[class="flex-1 flex-order-2 text-right"] [aria-label="Toggle navigation"]').click()
    main_page.element('[href="/login"]').click()
