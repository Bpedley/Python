import requests, bs4, os, time
from selenium import webdriver

req = input('Введите название категории: ')

driverpath = 'D:\\Python\\chromedriver.exe'
browser = webdriver.Chrome(driverpath)
browser.get('https://imgur.com')
time.sleep(3)
search = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[1]/div[1]/div[3]/div/form/input')
search.send_keys(req)
search.submit()
time.sleep(3)

url = browser.current_url
os.chdir('D:')
os.makedirs('D:\\imgur', exist_ok=True)

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

picElem = soup.select('.image-list-link img')

for image in range(len(picElem)):
    picUrl = 'http:' + picElem[image].get('src')
    # Download the image.
    print('Downloading image %s' % (picUrl))
    res = requests.get(picUrl)
    res.raise_for_status()
    
    imageFile = open(os.path.join('imgur', os.path.basename(picUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

print('Done.')