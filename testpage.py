from baseapp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators():
    dc = {}
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        dc[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        dc[locator] = (By.CSS_SELECTOR, locators["css"][locator])
    for locator in locators["name"].keys():
        dc[locator] = (By.CLASS_NAME, locators["name"][locator])


class OperationHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {locator}')
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator

        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f'Exception with click')
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):

        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=10)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get test from {element_name}')
            return None
        logging.debug(f'We find text {text} in field {element_name}')
        text = field.text

        return text

        # ENTER
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.dc["LOCATOR_LOGIN_FIELD"], word,
                                       description="Login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.dc["LOCATOR_PASS_FIELD"], word,
                                       description="Password form")



    # CLICK

    def click_login_button(self):
        self.click_button(TestSearchLocators.dc["LOCATOR_LOGIN_BTN"], description="login")

    def click_about(self):
        self.click_button(TestSearchLocators.dc["LOCATOR_ABOUT_BTN"], description="About")



    # GET TEXT

    def get_about_text(self):
        return self.get_text_from_element(TestSearchLocators.dc["LOCATOR_FONT_FIELD"], description="About Page")

    # GET PROPERTY
    def get_property(self):
        return self.get_element_property(TestSearchLocators.dc["LOCATOR_FON_FIELD"], "font-size")

