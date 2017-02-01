from __future__ import absolute_import

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import base64
import os
import unittest


url = "url goes here"
user_account = "NPATestUser@bna.com"


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(BusinessSystemsPortalTest('test_site_accessible'))
    return test_suite


class BusinessSystemsPortalTest(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox()
        # self.driver = webdriver.Ie() # doesn't work
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)
        self.driver.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()
        os.system('tskill phantomjs')  # workaround to close phantomjs since quit() doesnt do everything

    def test_site_accessible(self):
        self.driver.get(url)
        try:
            login_box = self.driver.wait.until(ec.presence_of_element_located((By.NAME, "login")))
            login_box.send_keys(user_account)
            password_box1 = self.driver.wait.until(ec.presence_of_element_located((By.NAME, "passwd")))
            password_box1.click()  # needed to proceed to actual login screen
            password_box2 = self.driver.wait.until(ec.presence_of_element_located((By.NAME, "Password")))
            password_file = open("../etc/user_pass.txt", 'r')  # SHOULD ONLY BE READABLE BY APPLICATION USER!!!
            password = base64.b64decode(password_file.read())
            password_box2.send_keys(password)
            submit_button = self.driver.wait.until(ec.element_to_be_clickable((By.ID, "submitButton")))
            submit_button.click()
            title = self.driver.wait.until(ec.presence_of_element_located((By.CLASS_NAME, "BNATeamSiteTitle")))
            self.assertEquals(str(title.text), "Business Systems")
            self.assertEquals(str(self.driver.title), "Business Systems - Home")  # there is a typo in the site title...
        except TimeoutException:
            self.fail("Box or dropdown not found")


if __name__ == "__main__":
    unittest.main()
