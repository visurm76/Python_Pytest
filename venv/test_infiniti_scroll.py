# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:15:42 2022

@author: VSurmin
"""
import pytest
import time
import utils as u

LINK = u.url['infiniti_scroll']


def test_infiniti_scroll(browser):
    browser.get(LINK)
    SCROLL_PAUSE_TIME = 0.5
    count = 0
    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        count += 1
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height or count == 3:
            break
        last_height = new_height
        time.sleep(7)
