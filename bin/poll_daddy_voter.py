from __future__ import absolute_import

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

url = "http://www.baltimoresun.com/news/maryland/howard/sports/"
url += "ph-hs-hoco-january-girls-bball-player-of-month-poll-20170131-htmlstory.html"

#TODO use tor (http://stackoverflow.com/questions/15316304/open-tor-browser-with-selenium)
# driver = webdriver.PhantomJS()
driver = webdriver.Firefox()
driver.wait = WebDriverWait(driver, 10)
driver.set_window_size(1120, 550)
driver.get(url)

#choice = driver.wait.until(ec.presence_of_element_located((By.ID, "PDI_answer44146137")))
#choice.click()
driver.find_element_by_id('PDI_answer44146137').click()

#vote_button = driver.wait.until(ec.presence_of_element_located((By.CLASS_NAME, "pds-vote-button")))
#vote_button.click()
driver.find_element_by_class_name("pds-vote-button").click()

driver.quit()
#os.system('tskill phantomjs')  # workaround to close phantomjs since quit() doesnt do everything