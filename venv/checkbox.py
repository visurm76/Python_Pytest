# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 09:52:23 2021

@author: VSurmin
"""
import time
from selenium import webdriver


try: 
    link = "https://the-internet.herokuapp.com/checkboxes"
    browser = webdriver.Chrome()
    browser.get(link)
    option_check_one = browser.find_element_by_css_selector("#checkboxes > input[type=checkbox]:nth-child(1)")
    option_check_one.click()
    option_check_tow = browser.find_element_by_css_selector("#checkboxes > input[type=checkbox]:nth-child(3)")
    option_check_tow.click()
finally:
    time.sleep(5)
    browser.quit()