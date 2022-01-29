import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import utils as u


LINK = u.url['digest_authentication']

def test_digest_authentication(browser):
    browser.get(LINK)
    browser.find_element(By.LINK_TEXT, "Имя пользователя").click()
    # Wait for the alert to be displayed
    wait.until(expected_conditions.alert_is_present())
    # Store the alert in a variable for reuse
    alert = Alert(browser)
    # Type your message
    alert.send_keys("Selenium")
    print("alert accepted")
    time.sleep(5)
