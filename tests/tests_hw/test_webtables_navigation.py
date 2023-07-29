import time

from pages.webtables import WebTables


def test_web_tables_navigation(browser):
    web_tables_page = WebTables(browser)
    first_name = 'Victoria'
    last_name = 'Gotovtseva'
    email = 'gtvcva@mail.ru'
    age = '25'
    salary = '100000'
    department = 'IT'

    web_tables_page.visit()
    web_tables_page.rows_five.click()


    assert web_tables_page.btn_previous.get_dom_attribute('disabled')
    assert web_tables_page.btn_next.get_dom_attribute('disabled')

    for i in range(3):
        web_tables_page.btn_add.click()
        web_tables_page.first_name.send_keys(first_name)
        web_tables_page.last_name.send_keys(last_name)
        web_tables_page.email.send_keys(email)
        web_tables_page.age.send_keys(age)
        web_tables_page.salary.send_keys(salary)
        web_tables_page.department.send_keys(department)
        web_tables_page.btn_submit.click()

    assert web_tables_page.total_pages.get_text() == '2'
    assert not web_tables_page.btn_next.get_dom_attribute('disabled')

    web_tables_page.btn_next.click()
    assert web_tables_page.current_page.get_dom_attribute('value') == '2'
    web_tables_page.btn_previous.click()
    assert web_tables_page.current_page.get_dom_attribute('value') == '1'

