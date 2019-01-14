#! python3
# webComic.py - program that checks the websites of several web comics
# and automatically downloads the images if the comic was updated since
# the program’s last visit.

import requests, os, bs4

url = 'http://xkcd.com'
os.chdir('D:\\')
os.makedirs('D:\\xkcd', exist_ok=True)

res = requests.get(url)
res.raise_for_status()


soup = bs4.BeautifulSoup(res.text, "lxml")

comicElem = soup.select('#comic img')

comicUrl = 'http:' + comicElem[0].get('src')

name = os.path.basename(comicUrl)


if os.path.isfile(name) == True:
    print('Already exists')
else:
    print('Adding')