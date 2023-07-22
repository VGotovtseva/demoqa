import time

from pages.text_box import TextBox


def test_clear(browser):
    text_box_page = TextBox(browser)

    text_box_page.visit()
    text_box_page.user_name.send_keys('victoria')
    time.sleep(2)
    text_box_page.user_name.clear()
    time.sleep(2)
    assert text_box_page.user_name.get_text() == ''


