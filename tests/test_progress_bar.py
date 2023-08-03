import time

from pages.progress_bar import ProgressBar


def test_progress_bar(browser):
    progress_bar_page = ProgressBar(browser)
    progress_bar_page.visit()
    time.sleep(2)

    progress_bar_page.btn_start.click()
    while True:
        if progress_bar_page.progress_bar.get_dom_attribute('aria-valuenow') == '51':
            progress_bar_page.btn_start.click()
            time.sleep(2)
            break
