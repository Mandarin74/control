import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml


with open('testdata.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    url = data['address']


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = url

    def find_element(self, locator, time=15):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")
        except:
            logging.exception("find element exception")
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.driver.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f"{property} not found in element")
        return None

    def go_to_site(self):
        try:
            start_browser = self.driver.get(self.base_url)
        except:
            logging.exception("exception while open site")
            start_browser = None
        return start_browser