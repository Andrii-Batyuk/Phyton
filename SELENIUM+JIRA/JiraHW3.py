from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from XPATH import footer_menu_xpath

# 1 Open site
driver = webdriver.Chrome()
driver.get('http://www.yanigen.com.ua/en')
driver.maximize_window()

# 2 Click Home on Main Menu
home_en_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, footer_menu_xpath.home_en)
    )
)
home_en_button.click()

# 3 Click PRODUCTS TO ORDER on Main Menu
products_to_order_en_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, footer_menu_xpath.products_to_order_en)
    )
)
products_to_order_en_button.click()

# 4 Click CATALOG on Main Menu
catalog_en_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, footer_menu_xpath.catalog_en)
    )
)
catalog_en_button.click()

# 5 Click TO CLIENTS on Main Menu
to_clients_en_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, footer_menu_xpath.to_clients_en)
    )
)
to_clients_en_button.click()

# 6 Click ABOUT US on Main Menu
about_us_en_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, footer_menu_xpath.about_us_en)
    )
)
about_us_en_button.click()

# 7 Click CONTACTS on Main Menu
contacts_en_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, footer_menu_xpath.contacts_en)
    )
)
contacts_en_button.click()

driver.quit()
