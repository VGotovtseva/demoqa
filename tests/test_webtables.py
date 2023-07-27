import time

from pages.webtables import WebTables


def test_web_tables(browser):
    web_tables_page = WebTables(browser)
    web_tables_page.visit()

    assert not web_tables_page.no_rows.exist()

    while web_tables_page.btn_delete_str.exist():
        web_tables_page.btn_delete_str.click()

    assert web_tables_page.no_rows.exist()


