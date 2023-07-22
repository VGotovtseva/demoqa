import time

from pages.text_box import TextBox


def test_text_box(browser):
    text_box_page = TextBox(browser)

    text_box_page.visit()

    text_box_page.user_name.send_keys('Test Test Test')
    text_box_page.current_address.send_keys('saint-petersburg')
    text_box_page.btn_submit.click_force()
    assert text_box_page.output_text.check_count_elements(2)


