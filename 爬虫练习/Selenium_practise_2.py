# selenium_class 2

from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/nbote/Downloads/chromedriver')
driver.fullscreen_window()
driver.get('http://www.google.com')

time.sleep(5)
driver.find_element_by_name('q').send_keys('www.163.com\n')

time.sleep(2)
driver.quit()
