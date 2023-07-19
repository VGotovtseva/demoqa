from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_check_text_footer(browser):
    home_page = DemoQa(browser)
    home_page.visit()

    assert home_page.footer_text.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_text_body(browser):
    home_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    home_page.visit()
    home_page.btn_elements.click()
    assert elements_page.body_text.get_text() == 'Please select an item from left to start practice.'

