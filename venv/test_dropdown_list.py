# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 13:03:52 2022

@author: VSurmin
"""
import pytest
import time
import utils as u


LINK = u.url['dropdown_list']

#Function 
def test_admin_authorization(browser):    
    browser.get(LINK)
    browser.implicitly_wait(5)
    #Search and click "Option 1"
    browser.find_element_by_css_selector("#dropdown > option:nth-child(2)").click()
    time.sleep(5)
    browser.find_element_by_css_selector("#dropdown > option:nth-child(3)").click()
    #Search and click "Option 2"
    time.sleep(7)
    