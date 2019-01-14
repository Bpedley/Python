from selenium import webdriver

driverpath = 'D:\\Python\\chromedriver.exe'
browser = webdriver.Chrome(driverpath)
type(browser)
browser.get('http://inventwithpython.com')