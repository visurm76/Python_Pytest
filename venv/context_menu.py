# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 10:22:09 2021

@author: VSurmin
"""

import time
from selenium import webdriver
from selenium.webdriver import ActionChains

try:
    LINK = "https://the-internet.herokuapp.com/context_menu"
    browser = webdriver.Chrome()
    action = ActionChains(browser)
    browser.get(LINK)
    #Search area for click right key (context menu)
    area_to_click = browser.find_element_by_css_selector("#hot-spot")
    #Click to area right key
    action.context_click(area_to_click).perform()
    #Confirm alert
    confirm = browser.switch_to.alert
    confirm.accept()
finally:
    time.sleep(10)
    browser.quit()
    