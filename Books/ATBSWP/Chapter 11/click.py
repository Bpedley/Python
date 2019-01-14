from selenium import webdriver

driverpath = 'D:\\Python\\chromedriver.exe'
browser = webdriver.Chrome(driverpath)
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Scratch Programming Playground')
print(type(linkElem))
linkElem.click()