#! python3
# cmd_email - Takes an email address and text and then logs into email
# account and sends an email to the provided address.

import sys, time
from selenium import webdriver

if len(sys.argv) > 2:
    # Get address, theme and text from command line.
    email = ''.join(sys.argv[1])
    theme = ''.join(sys.argv[2])
    text = ' '.join(sys.argv[3:])
else:
    print('Enter email, theme and text again')

login = input('Enter a login name: ')
passw = input('Enter a password: ')

driverpath = 'D:\\Python\\chromedriver.exe'
browser = webdriver.Chrome(driverpath)
browser.get('https://yandex.ru')

# Водйти в окно входа в почту
enterMail = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[1]/div/a[1]').click()

# Заполнение полей логина и пароля данными с коммандной строки
emailElem = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div/div/div/div/form/div[1]/label/input')
emailElem.send_keys(login)
passElem = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div/div/div/div/form/div[2]/label/input')
passElem.send_keys(passw)
passElem.submit()
time.sleep(7)

# Нажатие на кнопку написать письмо
write = browser.find_element_by_xpath('//*[@id="nb-1"]/body/div[3]/div[4]/div/div[2]/div[2]/div/div/a/span').click()
time.sleep(7)

# Заполнение поля адреса, темы и текста письма данными введенными в коммандоной строке 
name_email = browser.find_element_by_xpath('//*[@id="nb-1"]/body/div[3]/div[4]/div/div[3]/div[3]/div[2]/div[5]/div/div[1]/div[2]/div[1]/div/div[1]/label/div[3]/div')
name_email.send_keys(email)
theme_email = browser.find_element_by_xpath('//*[@id="nb-1"]/body/div[3]/div[4]/div/div[3]/div[3]/div[2]/div[5]/div/div[1]/div[2]/div[1]/div/label/div[3]/input')
theme_email.send_keys(theme)
text_email = browser.find_element_by_xpath('//*[@id="cke_1_contents"]/textarea')
text_email.send_keys(text)

# Отправка письма нажатием кнопки отправить
send_email = browser.find_element_by_xpath('//*[@id="nb-13"]/span/span/span').click()
