# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:29:51 2022

@author: VSurmin
"""
import time

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import utils as u

LINK = u.url['jquery_menu_v_1']


def test_jquery_menu_v_1(browser):
    browser.get(LINK)
    # Search for the jquery menu of the "Enable" button
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ui-id-3 > a"))).click()
    # Search for the jquery menu of the "Download" button
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ui-id-4 > a"))).click()
    # Search for the jquery menu of the "PDF" button
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ui-id-5 > a"))).click()
    time.sleep(5)
