# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 13:49:32 2022

@author: VSurmin
"""
import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
