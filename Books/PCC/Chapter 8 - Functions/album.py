
def make_album(artist_name, title, tracks=''):
    '''Return a dictionary of information about a artist.'''
    artist = {'name': artist_name, 'album': title}
    if tracks:
        artist['tracks'] = tracks
    return artist


musician1 = make_album('Mike', 'Hero')
musician2 = make_album('Mike', 'Hero', 15)
print(musician1)
print(musician2)

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    name = input("Name: ")
    if name == 'q':
        break
    album = input("Album name: ")
    if album == 'q':
        break
    name_album = make_album(name, album)
    print(name_album)