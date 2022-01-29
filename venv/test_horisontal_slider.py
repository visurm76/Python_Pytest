# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:32:35 2022

@author: VSurmin
"""

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import utils as u

LINK = u.url['horisontal_slider']


def test_horisontal_slider(browser):
    browser.get(LINK)
    time.sleep(3)
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable \
             ((By.CSS_SELECTOR, "#content > div > div > input[type=range]"))).click()
    action = webdriver.ActionChains(browser)
    for _ in range(2):
        action.send_keys(Keys.ARROW_RIGHT)
        time.sleep(2)
    action.perform()
