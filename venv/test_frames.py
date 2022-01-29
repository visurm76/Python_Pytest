# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:25:36 2022

@author: VSurmin
"""
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utils as u

LINK = u.url['frames']


def test_frames(browser):
    browser.get(LINK)
    # search for the "iframe" link     
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable \
             ((By.CSS_SELECTOR, "#content > div > ul > li:nth-child(2) > a"))).click()
    text = "Привет лунатикам!"
    # active iframe
    WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="mce_0_ifr"]')))
    browser.find_element_by_css_selector('#tinymce').click()
    text_area = browser.find_element_by_css_selector('#tinymce')
    text_area.clear()
    browser.find_element_by_css_selector('#tinymce').send_keys(text)
    time.sleep(7)
