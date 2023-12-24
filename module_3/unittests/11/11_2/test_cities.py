'''11.2. Население: измените свою функцию так, чтобы у нее был третий 
обязательный параметр —  население. В новой версии функция должна возвращать
одну строку вида «Santiago, Chile —  population 5 000 000». Снова запустите
программу test_cities.py. Убедитесь в том, что тест test_city_country() на этот
раз не проходит. Измените функцию так, чтобы параметр населения стал 
необязательным. Снова запустите test_cities.py и убедитесь в том, что тест 
test_city_country() снова проходит успешно. Напишите второй тест 
test_city_country_population(), который проверяет вызов функции со значениями 
'santiago', 'chile' и 'population=5000000'. Снова запустите test_cities.
py и убедитесь в том, что новый тест проходит успешно.'''

import unittest
from city_function import get_city_country

class CityCountryTest(unittest.TestCase):
    
    def test_city_country(self):
        correct_info = get_city_country('madrid', 'spain')
        self.assertEqual(correct_info, 'Madrid, Spain')
    
    def test_city_country_population(self):
        correct_info = get_city_country('santiago', 'chile', 5000000)
        self.assertEqual(correct_info, 'Santiago, Chile —  population 5000000')

if __name__ == '__main__':
    unittest.main()