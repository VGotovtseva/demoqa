import time

from pages.modal_dialogs import ModalDialogs


def test_check_modal(browser):
    modal_page = ModalDialogs(browser)
    modal_page.visit()

    assert modal_page.small_modal.exist() \
           and modal_page.small_modal.get_text() == 'Small modal'
    assert modal_page.large_modal.exist() \
           and modal_page.large_modal.get_text() == 'Large modal'

    modal_page.small_modal.click()
    assert modal_page.modal_form.visible()
    assert modal_page.small_modal_close.exist() \
           and modal_page.small_modal_close.get_text() == 'Close'
    modal_page.small_modal_close.click()
    assert not modal_page.modal_form.exist()

    modal_page.large_modal.click()
    assert modal_page.modal_form.visible()
    assert modal_page.large_modal_close.exist() \
           and modal_page.large_modal_close.get_text() == 'Close'
    modal_page.large_modal_close.click()
    assert not modal_page.modal_form.exist()



