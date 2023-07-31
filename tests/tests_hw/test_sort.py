import time

from pages.webtables import WebTables


def test_sort(browser):
    web_tables_page = WebTables(browser)
    web_tables_page.visit()
    for element in web_tables_page.th_table.find_elements():
        element.click()
        assert "sort-asc" in element.get_dom_attribute("class")
        #time.sleep(2)

