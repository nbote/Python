# selenium

from selenium import webdriver

driver = webdriver.Chrome('/Users/nbote/Downloads/chromedriver')
driver.fullscreen_window()
driver.get('http://www.amazon.com')
driver.find_element_by_id("nav-your-amazon").click()

driver.quit()
