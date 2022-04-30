from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from XPATH import money_menu_xpath

# 1 Open site
driver = webdriver.Chrome()
driver.get('http://www.yanigen.com.ua/ru')
driver.maximize_window()

# 2 Click dollar currency
dollar_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, money_menu_xpath.dollar)
    )
)
dollar_button.click()

# 3 Click hryvna currency
hryvna_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, money_menu_xpath.hryvna)
    )
)
hryvna_button.click()

# 4 close the site
driver.close()
