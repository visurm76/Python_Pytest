# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:09:31 2022

@author: VSurmin
"""

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import utils as u

LINK = u.url['hovers']


def test_hovers(browser):
    # Navigate to url
    browser.get(LINK)
    # Store 'google search' button web element
    searchBtn = browser.find_element(By.CSS_SELECTOR, "#content > div > div:nth-child(3) > img")
    # Perform click-and-hold action on the element
    webdriver.ActionChains(browser).click_and_hold(searchBtn).perform()
    time.sleep(2)
    searchBtn = browser.find_element(By.CSS_SELECTOR, "#content > div > div:nth-child(4) > img")
    # Perform click-and-hold action on the element
    webdriver.ActionChains(browser).click_and_hold(searchBtn).perform()
    time.sleep(2)
    searchBtn = browser.find_element(By.CSS_SELECTOR, "#content > div > div:nth-child(5) > img")
    # Perform click-and-hold action on the element
    webdriver.ActionChains(browser).click_and_hold(searchBtn).perform()
    time.sleep(5)
