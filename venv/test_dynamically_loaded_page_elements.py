# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 13:41:28 2022

@author: VSurmin
"""

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utils as u

LINK = u.url['dynamically_loaded_page_elements']
example = {'example_one': "#content > div > a:nth-child(5)",
           'example_tow': "#content > div > a:nth-child(8)"}


def test_dynamically_loaded_page_elements_example_1(browser):  # The function of working with links
    browser.get(LINK)
    time.sleep(3)
    # Waiting for the modal window to become active and click "Example 1"
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, example['example_one']))).click()
    time.sleep(3)
    # Click button "Start".
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#start > button"))).click()
    time.sleep(3)


def test_dynamically_loaded_page_elements_example_2(browser):  # The function of working with links
    browser.get(LINK)
    time.sleep(3)
    # Waiting for the modal window to become active and click "Example 1"
    # or "Example 2".
    # Waiting for the modal window to become active and click "Example 1"
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, example['example_tow']))).click()
    time.sleep(3)
    # Click button "Start".
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#start > button"))).click()
    time.sleep(3)
