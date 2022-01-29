# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:35:11 2022

@author: VSurmin
"""

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import utils as u


LINK = u. utils['jquery_menu_v_2']

def test_jquery_menu_v_1(browser):    
    browser.get(LINK)    
    # Search for the jquery menu of the "Enable" button
    searchBtn = WebDriverWait(browser, 20).until(EC.visibility_of_element_located\
        ((By.CSS_SELECTOR, "#ui-id-3 > a")))
    webdriver.ActionChains(browser).move_to_element(searchBtn).perform()
        # Search for the jquery menu of the "Download" button
    searchDownload = WebDriverWait(browser, 20).until(EC.visibility_of_element_located\
        ((By.CSS_SELECTOR, "#ui-id-4 > a")))
    webdriver.ActionChains(browser).move_to_element(searchDownload).perform()
        #Search for the jquery menu of the "PDF" button
    searchPDF = WebDriverWait(browser, 20).until(EC.visibility_of_element_located\
        ((By.CSS_SELECTOR, "#ui-id-5 > a")))
    webdriver.ActionChains(browser).move_to_element(searchPDF).click().perform()