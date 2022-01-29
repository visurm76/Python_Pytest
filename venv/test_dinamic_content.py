# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 08:46:39 2022

@author: VSurmin
"""
import time
import pytest
from selenium import webdriver
import utils as u


LINK = u.url['dinamic_content']

def test_dinamic_content(browser):
    browser.get(LINK)
    browser.implicitly_wait(5)
    #Creating lists
    text_list_old = []
    text_list_new = []
    #Function search text elements
    def contents(a):
        elements = browser.find_elements_by_css_selector \
        ('#content  > .example > .row  > #content > .row > .large-10')
        for elem in range(len(elements)):
            a.append(elements[elem].text)
        return a
    text_list_old_set = set(contents(text_list_old))
    #wait 5 sec
    time.sleep(5)
    #Click refresh button
    click_button = browser.find_element_by_xpath('//*[@id="content"]/div/p[2]/a').click()
    #Updated content
    text_list_new_set = set(contents(text_list_new))
    #Wait 5 sec
    time.sleep(5)
    #Search for non-matching content
    differences_set = (text_list_new_set.difference(text_list_old_set))
    DIFFERRNCES_TEXT = " ".join(differences_set)
    return print(DIFFERRNCES_TEXT)
