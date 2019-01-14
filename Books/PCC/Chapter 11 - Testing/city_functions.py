def city_country(city, country, population=''):
    if population:
        full_city_country = city.title() + ', ' + country.title() + ' - population ' + str(population) + '.'
    else:
        full_city_country = city.title() + ', ' + country.title()
    return full_city_country