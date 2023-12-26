import time
from testpage import OperationHelper
import logging
import yaml

with open("testdata.yaml", encoding="utf-8") as f:
    data = yaml.safe_load(f)


def test_step_1(browser):
    logging.info("Test1 starting")
    test_page = OperationHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(data["log"])
    test_page.enter_pass(data["pass"])
    test_page.click_login_button()
    test_page.click_about()
    time.sleep(5)
    assert test_page.get_about_text() == "About Page"


def test_step_2(browser):
    logging.info("Test1 starting")
    test_page = OperationHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(data["log"])
    test_page.enter_pass(data["pass"])
    test_page.click_login_button()
    test_page.click_about()
    time.sleep(5)
    assert test_page.get_property() == "32px"
