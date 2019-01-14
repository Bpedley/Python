from selenium import webdriver

driverpath = 'D:\\Python\\chromedriver.exe'
browser = webdriver.Chrome(driverpath)
browser.get('https://mail.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('not_my_real_email')
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys('12345')
passwordElem.submit()