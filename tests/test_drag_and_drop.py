import time

from pages.droppable import Droppable
from selenium.webdriver import ActionChains


def test_drag_and_drop(browser):
    droppable_page = Droppable(browser)
    droppable_page.visit()

    assert not droppable_page.drop.get_dom_attribute('background-color')
    action_chains = ActionChains(browser)
    action_chains.drag_and_drop(droppable_page.drag.find_element(), droppable_page.drop.find_element()).perform()
    time.sleep(2)

    assert droppable_page.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')

    action_chains.drag_and_drop_by_offset(droppable_page.drag.find_element(), -300, 0).perform()
    time.sleep(2)

    assert droppable_page.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')