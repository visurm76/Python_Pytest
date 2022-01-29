# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:10:57 2022

@author: VSurmin
"""

import pytest
import time
import utils as u


LINK = u.url['file_download']

def test_file_download(browser):    
    browser.get(LINK)
    time.sleep(3)
    browser.implicitly_wait(7)
    links = []
    # Import a list of file names
    element_txt = browser.find_elements_by_xpath('//*[@id="content"]/div/a')
    # Adding a list of file names.
    for elem in range(len(element_txt)):
        links.append(element_txt[elem].text)
    # Click on the link
    for file in links:
        f = browser.find_element_by_partial_link_text(file).click()
        time.sleep(5)

   