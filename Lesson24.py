import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as SF
from selenium.webdriver.chrome.service import Service as SC
driver_path_chrome = SC(os.getcwd() + '\drivers\chromedriver.exe')
driver_path_firefox = SF(os.getcwd() + '\drivers\geckodriver.exe')


driver = webdriver.Firefox(service=driver_path_firefox)



# url = 'http://svetlyachok.mk.ua'
url = 'https://test.mensa.no/'
driver.get(url)
driver.set_window_position(-1920, 0)
# time.sleep(5)
driver.maximize_window()

print(driver.title)

button_18_50 = '/html/body/div[2]/main/cach/div[1]/div/div/div[2]/div/button[2]'
button_51_60 = '/html/body/div[2]/main/cach/div[1]/div/div/div[2]/div/button[3]'

button_start = driver.find_element('xpath', button_18_50)
button_start.click()
time.sleep(5)
button_start_test = '//*[@id="startTest"]'
button_start_test = driver.find_element('xpath', button_start_test)
button_start_test.click()
time.sleep(5)
button_pass_test1 = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_pass_test1 = driver.find_element('xpath', button_pass_test1)
button_pass_test1.click()
time.sleep(5)
button_pass_test2 = '/html/body/div[2]/main/cach/div[3]/div[5]/div[3]/div[5]/div/img'
button_pass_test2 = driver.find_element('xpath', button_pass_test2)
button_pass_test2.click()
time.sleep(5)
button_pass_test3 = '/html/body/div[2]/main/cach/div[3]/div[2]/div[3]/div[6]/div/img'
button_pass_test3 = driver.find_element('xpath', button_pass_test3)
button_pass_test3.click()



# driver.quit()

# driver = webdriver.Firefox(service=driver_path_firefox)
# #driver = webdriver.Chrome(service=driver_path_chrome)
# url = 'https://core.telegram.org/'
# driver.get(url)
# # driver.set_window_position(1600,300)#Для второго монитора расположенного справа
# time.sleep(2)
# driver.maximize_window()
# #HEADLESS БЕЗГОЛОВЫЙ Режим работы без визуального запуска
# # driver.set_window_size(300,100)
# url = 'https://test.mensa.no/'
# driver.get(url)
# print(driver.title)
# button_18_50_xpath = '/html/body/div[2]/main/cach/div[1]/div/div/div[2]/div/button[2]'
# button_51_60_xpath = '/html/body/div[2]/main/cach/div[1]/div/div/div[2]/div/button[3]'
# button_51_60 = driver.find_element('xpath',button_51_60_xpath)
# print(button_51_60.text)
# button_18_50 = driver.find_element('xpath',button_18_50_xpath)
# print(button_18_50.text)
# time.sleep(2)
# button_18_50.click()
# button_start_xpath = '//*[@id="startTest"]'
# button_start_xpath_full = '/html/body/div[2]/main/cach/div[2]/div/div/div/div[2]/button'
# button_start = driver.find_element('xpath',button_start_xpath_full)
# time.sleep(2)
# button_start.click()