cities = {
    'Moscow': {
        'country': 'Russia',
        'population': '12 000 000',
        'fact': 'City Of Billionaires',
    },
    'Los Angeles': {
        'country': 'USA',
        'population': '4 000 000',
        'fact': 'The Hollywood sign originally said "Hollywoodland"',
    },
    'New York': {
        'country': 'USA',
        'population': '8 500 000',
        'fact': 'New York City has 722 miles of subway track',
    },
}

for city, city_info in cities.items():
    print('City: ' + city)
    print('Country: ' + city_info['country'])
    print('Population: ' + city_info['population'])
    print('Fact about ' + city + ': ' + city_info['fact'] + '\n')