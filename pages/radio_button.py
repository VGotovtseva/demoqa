from pages.base_page import BasePage
from components.components import WebElement


class RadioButton(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)
        self.radio_yes = WebElement(driver, '#yesRadio')
        self.radio_no = WebElement(driver, '#noRadio')
        self.radio_impressive = WebElement(driver, '#impressiveRadio')
        self.radio_text = WebElement(driver, '.mt-3')








