import time

from pages.webtables import WebTables
from selenium.webdriver.common.keys import Keys


def test_webtables(browser):
    web_tables_page = WebTables(browser)
    first_name = 'Victoria'
    last_name = 'Gotovtseva'
    email = 'gtvcva@mail.ru'
    age = '25'
    salary = '100000'
    department = 'IT'
    edited_first_name = '!'

    web_tables_page.visit()

    assert web_tables_page.btn_add.exist()
    web_tables_page.btn_add.click()

    assert web_tables_page.modal_dialog.exist()

    web_tables_page.btn_submit.click()
    assert web_tables_page.modal_form.get_dom_attribute('class') == 'was-validated'

    web_tables_page.first_name.send_keys(first_name)
    web_tables_page.last_name.send_keys(last_name)
    web_tables_page.email.send_keys(email)
    web_tables_page.age.send_keys(age)
    web_tables_page.salary.send_keys(salary)
    web_tables_page.department.send_keys(department)
    web_tables_page.btn_submit.click()

    assert not web_tables_page.modal_dialog.exist()

    assert web_tables_page.added_first_name.get_text() == first_name
    assert web_tables_page.added_last_name.get_text() == last_name
    assert web_tables_page.added_email.get_text() == email
    assert web_tables_page.added_age.get_text() == age
    assert web_tables_page.added_salary.get_text() == salary
    assert web_tables_page.added_department.get_text() == department

    web_tables_page.btn_edit.click_force()
    assert web_tables_page.edit_modal_form.exist()

    web_tables_page.first_name.send_keys(edited_first_name)
    web_tables_page.btn_edit_submit.click()
    assert web_tables_page.added_first_name.get_text() == first_name+edited_first_name

    web_tables_page.btn_delete.click_force()
    assert web_tables_page.added_first_name.get_text() == ' '
    assert web_tables_page.added_last_name.get_text() == ' '
    assert web_tables_page.added_email.get_text() == ' '
    assert web_tables_page.added_age.get_text() == ' '
    assert web_tables_page.added_salary.get_text() == ' '
    assert web_tables_page.added_department.get_text() == ' '

