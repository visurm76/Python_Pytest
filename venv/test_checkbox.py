import time
import pytest
from selenium.webdriver.common.by import By
import utils as u

LINK = u.url['checkbox']


def test_checkbox(browser):
    browser.get(LINK)
    time.sleep(5)
    option_check_one = browser.find_element(By.CSS_SELECTOR,"#checkboxes > input[type=checkbox]:nth-child(1)").click()
    time.sleep(5)
    option_check_tow = browser.find_element(By.CSS_SELECTOR,"#checkboxes > input[type=checkbox]:nth-child(3)").click()
    time.sleep(5)


