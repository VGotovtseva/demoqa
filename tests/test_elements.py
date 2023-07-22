import time

from pages.elements_page import ElementsPage

from pages.check_box import CheckBox

from components.components import WebElement


def test_find_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()

    assert elements_page.btns_first_menu.check_count_elements(9)


def test_count_checkbox(browser):
    check_box_page = CheckBox(browser)

    check_box_page.visit()
    assert check_box_page.check_box.check_count_elements(1)

    check_box_page.option_plus.click()
    time.sleep(3)
    assert check_box_page.check_box.check_count_elements(17)

    for element in check_box_page.check_box.find_elements():
        assert element.is_displayed() #в данном случае обращаемся как объекту найденному в find_element

    check_box_page.refresh()
    assert check_box_page.check_box.check_count_elements(1)

    