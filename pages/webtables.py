from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_form = WebElement(driver, '#userForm')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.added_str = WebElement(driver, 'div.rt-tbody > div:nth-child(4)')
        self.added_first_name = WebElement(driver, 'div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.added_last_name = WebElement(driver, 'div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(2)')
        self.added_email = WebElement(driver, 'div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(4)')
        self.added_age = WebElement(driver, 'div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(3)')
        self.added_salary = WebElement(driver, 'div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(5)')
        self.added_department = WebElement(driver, 'div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(6)')
        self.btn_edit = WebElement(driver, '#edit-record-4')
        self.edit_modal_form = WebElement(driver, 'div.fade.modal.show > div')
        self.btn_edit_submit = WebElement(driver, '#submit')
        self.btn_delete = WebElement(driver, '#delete-record-4')








