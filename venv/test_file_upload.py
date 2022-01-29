# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:19:09 2022

@author: VSurmin
"""

import pytest
import time
import os
import utils as u

LINK = u.url['file_upload']


def test_file_upload(browser):
    browser.get(LINK)
    file_name = 'file.txt'
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_xpath('//*[@id="file-upload"]')
    element.send_keys(file_path)
    time.sleep(5)
