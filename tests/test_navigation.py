import time

from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_navigation(browser):
    home_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    home_page.visit()
    home_page.btn_elements.click()

    home_page.refresh()

    browser.refresh()
    browser.back()
    time.sleep(2)
    browser.forward()
    time.sleep(2)

    assert elements_page.equal_url()

