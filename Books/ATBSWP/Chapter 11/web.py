from selenium import webdriver

driverpath = 'D:\\Python\\chromedriver.exe'
browser = webdriver.Chrome(driverpath)
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('navbar-brand')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')