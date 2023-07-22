from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()

    assert modal_dialogs_page.btns_three_menu.check_count_elements(5)


def test_page_dialogs(browser):
    modal_dialogs_page = ModalDialogs(browser)


    modal_dialogs_page.visit()
    modal_dialogs_page.refresh()
    modal_dialogs_page.icon.click()
    modal_dialogs_page.back()

    browser.set_window_size(900, 400)
    modal_dialogs_page.forward()
    assert modal_dialogs_page.get_url() == 'https://demoqa.com/'
    assert modal_dialogs_page.get_title() == 'DEMOQA'

    browser.set_window_size(1000, 1000)
