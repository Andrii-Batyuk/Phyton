from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from XPATH import main_menu_xpath
import time

# 1 Open site
driver = webdriver.Chrome()
driver.get('http://www.yanigen.com.ua/en')
driver.maximize_window()

# 2 Click Home on Main Menu
home_en_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_menu_xpath.home_en)
    )
)
home_en_button.click()

# 3 Click PRODUCTS TO ORDER on Main Menu
products_to_order_en_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_menu_xpath.products_to_order_en)
    )
)
products_to_order_en_button.click()

# 4 Click CATALOG on Main Menu
catalog_en_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_menu_xpath.catalog_en)
    )
)
catalog_en_button.click()

# 5 Click TO CLIENTS on Main Menu
to_clients_en_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_menu_xpath.to_clients_en)
    )
)
to_clients_en_button.click()

# 6 Click submenu LOYALTY SYSTEM on element of menu TO CLIENTS
loyalty_system_en_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_menu_xpath.loyalty_system_en)
    )
)
loyalty_system_en_button.click()
time.sleep(2)

# 7 Click submenu CARE on element of menu TO CLIENTS
care_en_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_menu_xpath.care_en)
    )
)
care_en_button.click()
time.sleep(2)

# 8 Click submenu GUARANTEE on element of menu TO CLIENTS
guarantee_en = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_menu_xpath.guarantee_en)
    )
)
guarantee_en.click()
time.sleep(2)

# 8 Click submenu EXCHANGE AND RETURN on element of menu TO CLIENTS
exchange_and_return_en = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_menu_xpath.exchange_and_return_en)
    )
)
exchange_and_return_en.click()
time.sleep(2)

# 9 Click submenu PAYMENT AND DELIVERY on TO CLIENTS
payments_and_delivery_en_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_menu_xpath.payment_and_delivery_en)
    )
)
payments_and_delivery_en_button.click()


# 10 Click ABOUT US on Main Menu
about_us_en_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_menu_xpath.about_us_en)
    )
)
about_us_en_button.click()

# 11 Click CONTACTS on Main Menu
contacts_en_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_menu_xpath.contacts_en)
    )
)
contacts_en_button.click()

driver.quit()



ru_lang = '//li[@class]/a[contains(text(),"RU")]' #ru_button
eng_lang = '//li[@class]/a[contains(text(),"EN")]' #eng_button
ua_lang = '//li[@class]/a[contains(text(),"UA")]' #ua_button