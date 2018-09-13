# Selenium

from selenium import webdriver
import time

driver=webdriver.Chrome('/Users/nbote/Downloads/chromedriver')
driver.fullscreen_window()
driver.get('http://www.google.com')

driver.find_element_by_link_text('Gmail').click()

time.sleep(3)
driver.back()

driver.find_element_by_partial_link_text('mail').click()


time.sleep(5)
driver.quit()
