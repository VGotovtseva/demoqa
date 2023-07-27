import time

from pages.herokuapp import HeroKuapp
from pages.add_remove import AddRemove
from components.components import WebElement


def test_btn_add(browser):
    home_page = HeroKuapp(browser)
    add_remove_page = AddRemove(browser)
    home_page.visit()
    assert home_page.add_remove_elements.get_text() == 'Add/Remove Elements'

    home_page.add_remove_elements.click()
    time.sleep(2)
    
    assert add_remove_page.equal_url()

    assert add_remove_page.btn_add.get_text() == 'Add Element' \
           and add_remove_page.btn_add.get_dom_attribute('onclick') == 'addElement()'

    for i in range(4):
        add_remove_page.btn_add.click()

    time.sleep(2)

    assert add_remove_page.btn_delete.check_count_elements(4)

    for element in add_remove_page.btn_delete.find_elements():
        assert element.text == 'Delete' #было add_remove_page.btn_delete.get_text()
        element.click()

    assert not add_remove_page.btn_delete.exist()

    #while add_remove_page.btn_delete.exist():  вариант решения 3 задания
    #add_remove_page.btn_delete.click()



