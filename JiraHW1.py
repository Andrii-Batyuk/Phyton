from selenium import webdriver
import time

# 1 Open site yanigen.com.ua
driver = webdriver.Chrome()
driver.get('http://www.yanigen.com.ua')

# 2 Maximize window
driver.maximize_window()

# 3 Close site
time.sleep(10)
driver.close()