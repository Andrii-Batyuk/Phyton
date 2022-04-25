from selenium import webdriver


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
driver = webdriver.Chrome()
driver.get('http://yanigen.com.ua/ru/productstoder')

home_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, home_ru)
    )
)
home_ru_button.click()