favorite_places = {
    'jen': ['threatre', 'cinema'],
    'sarah': ['museum'],
    'edward': ['zoo', 'forest', 'coliseum'],
}
for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())