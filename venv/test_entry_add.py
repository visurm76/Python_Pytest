# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:45:55 2022

@author: VSurmin
"""
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utils as u


LINK = u.url['entry_add']

def test_entry_add(browser):   
    browser.get(LINK)    
    time.sleep(5)
    WebDriverWait(browser, 20).until \
    (EC.element_to_be_clickable \
    ((By.CSS_SELECTOR, "#modal > div.modal > div.modal-footer > p"))).click()

    