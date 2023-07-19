from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_go_to_page_elements(browser):
    home_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    home_page.visit()
    assert home_page.equal_url()

    home_page.btn_elements.click()
    assert elements_page.equal_url()




