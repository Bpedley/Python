import bs4

'''
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features='html.parser')
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)
'''

'''
pElems = exampleSoup.select('p')
print(len(pElems))
print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())
'''

soup = bs4.BeautifulSoup(open('example.html'), features='html.parser')
spanElem = soup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') == None)
print(spanElem.attrs)
