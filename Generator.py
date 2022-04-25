#
# for i in 6:
#     for a in list:

#Digital counter
from selenium import webdriver
a = 0
while a < 100000:
    print(a)
    driver = webdriver.Firefox()
    driver.get(f'https://prnt.sc/{a}')
    driver.get_screenshot_as_file(f'd{a}.png')
    driver.quit()
    a += 1




# driver = webdriver.Chrome()
# driver.get('http://svetlyachok.mk.ua')
# driver.quit()