def city_country(name, country):
    full = name + ', ' + country
    return full.title()

mike = city_country('Moscow', 'Russia')
dan = city_country('New York', 'USA')
alice = city_country('Paris', 'France')

print(mike)
print(dan)
print(alice)
