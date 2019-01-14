import requests, bs4

url = input('Enter site url: ')
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('a')
bad_links = []   # List of links that lead to a 404 page

for link in links:
    try:
        url1 = link['href']
        if url1.startswith("http:") or url1.startswith("https:") or url1.startswith('//'):
            url2 = url1
        elif url1.startswith('/'):
            url2 = url + url1
        else:
            url2 = url1

        result = requests.get(url2)

        if result.status_code == 404:
            bad_links.append(url2)
    except:
        pass

if len(bad_links) == 0:
    print('All links are valid.')
else:
    print('Links processed these ' + str(len(bad_links)) + ' returned error 404: ')
    print('\n'.join(bad_links))