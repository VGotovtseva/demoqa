from pages.base_page import BasePage
from components.components import WebElement


class CheckBox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/checkbox'
        super().__init__(driver, self.base_url)

        self.check_box = WebElement(driver, '.rct-text')
        self.option_plus = WebElement(driver, '.rct-option-expand-all')










