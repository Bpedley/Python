#! python3
# webComic.py - program that checks the websites of several web comics
# and automatically downloads the images if the comic was updated since
# the program’s last visit.

import requests, os, bs4

url = 'http://xkcd.com'
os.chdir('D:\\')
os.makedirs('D:\\xkcd', exist_ok=True)

print('Downloading page %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "lxml")

comicElem = soup.select('#comic img')
while :
if comicElem == []:
        print('Could not find comic image.')
else:
    try:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
    except requests.exceptions.MissingSchema:
        # skip this comic
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
        continue

    # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')