from __future__ import absolute_import

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


def init_driver():
    driver = webdriver.Firefox()
    # driver = webdriver.Ie()
    # driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def lookup(driver, query):
    driver.get("http://www.google.com")
    try:
        box = driver.wait.until(ec.presence_of_element_located((By.NAME, "q")))
        box.send_keys(query)
        button = driver.wait.until(ec.element_to_be_clickable((By.NAME, "btnG")))
        button.click()
    except TimeoutException:
        print("Box or Button not found in google.com")


if __name__ == "__main__":
    browser = init_driver()
    lookup(browser, "Selenium")
    time.sleep(5)
    browser.quit()
    # os.system('tskill Firefox')  # workaround to close firefox without hang
    # os.system('tskill geckodriver')
