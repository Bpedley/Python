from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driverpath = 'D:\\Python\\chromedriver.exe'
browser = webdriver.Chrome(driverpath)

browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)    # scrolls to bottom
browser.refresh()
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)
htmlElem.send_keys(Keys.UP)
htmlElem.send_keys(Keys.UP)
browser.quit()