from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement


class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.footer_text = WebElement(driver, 'footer > span')
        super().__init__(driver, self.base_url)






