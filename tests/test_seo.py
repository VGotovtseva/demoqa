import time

import pytest

from pages.demoqa import DemoQa
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab


def test_seo_title(browser):
    home_page = DemoQa(browser)

    home_page.visit()
    assert home_page.get_title() == 'DEMOQA'


@pytest.mark.parametrize('pages', [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'
