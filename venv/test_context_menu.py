import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import utils as u

LINK = u.url['context_menu']
def test_context_menu(browser):
    action = ActionChains(browser)
    browser.get(LINK)
    # Search area for click right key (context menu)
    area_to_click = browser.find_element(By.CSS_SELECTOR,"#hot-spot")
    time.sleep(5)
    # Click to area right key
    action.context_click(area_to_click).perform()
    time.sleep(5)
    # Confirm alert
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(5)