import pytest

from pages.demoqa import DemoQa
from pages.radio_button import RadioButton

@pytest.mark.skip
def test_decor(browser):
    home_page = DemoQa(browser)
    home_page.visit()
    assert home_page.h5_elements.check_count_elements(6)

    for element in home_page.h5_elements.find_elements():
        assert not element.text == ""

#@pytest.mark.skipif(True, reason= " ")
def test_radio_btn(browser):
    radio_btn_page = RadioButton(browser)

    if radio_btn_page.code_status() != 400:
        pytest.skip()
    else:
        radio_btn_page.visit()

    radio_btn_page.radio_yes.click_force()
    assert radio_btn_page.radio_text.get_text() == 'You have selected ' + 'Yes'
    radio_btn_page.radio_impressive.click_force()
    assert radio_btn_page.radio_text.get_text() == 'You have selected ' + 'Impressive'

    assert 'disabled' in radio_btn_page.radio_no.get_dom_attribute('class')


