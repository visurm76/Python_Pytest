# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 12:59:23 2022

@author: VSurmin
"""
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import utils as u

LINK = u.url['drag_drop']


def test_drag_drop(browser):
    browser.maximize_window()
    sourceEle = WebDriverWait(browser, 20).until(EC.element_to_be_clickable(By.ID, "column-a"))
    # Store 'box B' as source element
    targetEle = WebDriverWait(browser, 20).until(EC.element_to_be_clickable(By.ID, "column-b"))
    # Performs drag and drop action of sourceEle onto the targetEle
    webdriver.ActionChains(browser).drag_and_drop(sourceEle, targetEle).perform()
