from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from XPATH import language_menu_xpath

# 1 Open site
driver = webdriver.Chrome()
driver.get('http://www.yanigen.com.ua/ru')
driver.maximize_window()

# 2 Click EN language on footer Menu
english_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, language_menu_xpath.english)
    )
)
english_button.click()

# 3 Click RU language on footer Menu
russian_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, language_menu_xpath.russian)
    )
)
russian_button.click()

# 4 Click UA language on footer Menu
ukrainian_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, language_menu_xpath.ukrainian)
    )
)
ukrainian_button.click()

# 5 close the site
driver.close()
