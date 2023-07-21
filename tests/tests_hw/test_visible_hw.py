import time

from pages.accordion import Accordion


def test_visible_accordion(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert accordion_page.card_body_section1_content.visible()

    accordion_page.card_header_section1.click()
    time.sleep(2)
    assert not accordion_page.card_body_section1_content.visible()


def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()

    assert not accordion_page.card_body_section2_content1.visible()
    assert not accordion_page.card_body_section2_content2.visible()
    assert not accordion_page.card_body_section3_content.visible()




