# Selenium

from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/nbote/Downloads/chromedriver')
driver.fullscreen_window()
driver.get("http://www.baidu.com")  # 注意要用双引号

elements = driver.find_elements_by_tag_name('a')  # 注意是‘elements’

for element in elements:
    # print(element.text)
    if '新闻' in element.text:
        element.click()
        break

time.sleep(1)
driver.quit()
