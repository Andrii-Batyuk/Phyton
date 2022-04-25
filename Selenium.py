import os
from selenium import webdriver

driver_path_chrome = os.getcwd() + '/drivers/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path_chrome)
driver.get('https://www.yanigen.com.ua')
driver.get.screenshot_as_file('google.png')