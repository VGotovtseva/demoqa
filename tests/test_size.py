import time

from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_size(browser):
    home_page = DemoQa(browser)

    home_page.visit()

    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)


def test_visible_nav_bar(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert not elements_page.nav_bar.visible()

    browser.set_window_size(400, 699)
    assert elements_page.nav_bar.visible()

    browser.set_window_size(1000, 1000)
