from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.card_body_section1_content = WebElement(driver, '#section1Content > p')
        self.card_header_section1 = WebElement(driver, '#section1Heading')
        self.card_body_section2_content1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.card_body_section2_content2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.card_body_section3_content = WebElement(driver, '#section3Content > p')









