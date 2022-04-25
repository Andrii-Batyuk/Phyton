#Selenium webdriver
#
# from selenium import webdriver
# has = 'sadfds'
# driver = webdriver.Firefox()
# driver.get(f'https://prnt.sc/{has}')
# driver.get_screenshot_as_file(f'd{has}.png')
# driver.quit()
# # driver = webdriver.Chrome()
# # driver.get('http://svetlyachok.mk.ua')
# # driver.quit()

lis = '1' '2' '3' '4' '5' '6' '7' '8' '9' '0' 'a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z'
has = '00000'
listindex = 0
for i in range(len(lis)):
    for j in lis:
        print(j)
    has = f'{lis[i]}{lis[i]}{lis[i]}{lis[i]}{lis[i]}{lis[i]}'
    print(has)