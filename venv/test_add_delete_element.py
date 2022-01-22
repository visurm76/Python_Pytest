# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 15:43:13 2021

@author: VSurmin
"""
import time
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import utils as u


LINK = u.url['add_delete_element']
"""
Add and delete element
"""
def test_add_delete_elem(browser):
    #Search and click
    browser.get(LINK)
    time.sleep(5)
    add_element = browser.find_element(By.CSS_SELECTOR, "[onclick = 'addElement()']").click()
    time.sleep(5)
    delete_element = browser.find_element(By.CSS_SELECTOR, "#elements > button").click()

        