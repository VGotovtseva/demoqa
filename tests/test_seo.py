from pages.demoqa import DemoQa


def test_seo_title(browser):
    home_page = DemoQa(browser)

    home_page.visit()
    assert home_page.get_title() == 'DEMOQA'

