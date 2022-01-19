# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 15:43:13 2021

@author: VSurmin
"""
import time


"""
Add and delete element
"""
def test_add_delete_elem(open_browser):        
    #Waiting for clickability
    open_browser.\
        browser.implicitly_wait(5)
    #Search and click
    add_element = open_browser.browser.find_element_by_css_selector \
        ("[onclick = 'addElement()']").click()
    time.sleep(7)
    delete_element = open_browser.browser.find_element_by_css_selector \
        ("#elements > button").click()
        