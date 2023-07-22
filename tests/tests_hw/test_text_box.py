import time

from pages.text_box import TextBox


def test_text_box(browser):
    text_box_page = TextBox(browser)
    user_name = "TestTestTest"
    current_address = 'saint-petersburg'

    text_box_page.visit()

    text_box_page.user_name.send_keys(user_name)
    text_box_page.current_address.send_keys(current_address)
    text_box_page.btn_submit.click_force()
    assert text_box_page.output_text.check_count_elements(2)

    assert text_box_page.output_name.get_text()[5:] == user_name
    assert text_box_page.output_current_address.get_text()[17:] == current_address


