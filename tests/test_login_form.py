import time

from pages.form_page import FormPage
from selenium.webdriver.common.keys import Keys


def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)

    form_page.first_name.send_keys('victoria')
    form_page.last_name.send_keys('gotovtseva')
    form_page.user_email.send_keys('gtvcva@mail.ru')
    form_page.gender_radio_2.click_force()
    form_page.user_number.send_keys('9039815691')
    form_page.hobbies.click_force()
    form_page.current_address.send_keys('saint-petersburg')

    form_page.btn_submit.click_force()
    time.sleep(2)

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()


def test_fill_state_and_city(browser):
    form_page = FormPage(browser)

    form_page.visit()

    form_page.state.send_keys("Haryana" + Keys.ENTER)
    time.sleep(2)

    form_page.city.send_keys("Karnal" + Keys.ENTER)
    time.sleep(2)



