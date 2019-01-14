import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Test for 'city_functions.py'."""
    
    def test_city_country(self):
        formatted_city_country = city_country('moscow', 'russia')
        self.assertEqual(formatted_city_country, 'Moscow, Russia')

    def test_city_country_population(self):
        formatted_city_country = city_country('moscow', 'russia', 10000000)
        self.assertEqual(formatted_city_country, 'Moscow, Russia - population 10000000.')

unittest.main()