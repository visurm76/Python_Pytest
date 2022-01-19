# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 13:49:32 2022

@author: VSurmin
"""
import pytest
import utils as u

@pytest.fixture
def open_browser():
    LINK = u.url['add_delete_element']
    browser = u.browser
    browser.get(LINK )
    yield browser
    browser.quit()
