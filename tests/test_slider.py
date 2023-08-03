from pages.slider import Slider
from selenium.webdriver import ActionChains

def test_slider(browser):
    slider_page = Slider(browser)
    action_chains = ActionChains(browser)

    slider_page.visit()

    assert slider_page.slider.exist()
    assert slider_page.text.exist()
    assert slider_page.slider.get_dom_attribute('value') == '25'

    action_chains.drag_and_drop_by_offset(slider_page.slider.find_element(), 0, 1).perform()

    assert slider_page.text.get_dom_attribute('value') == '50'

