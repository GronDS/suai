'''11.1. Город, страна: напишите функцию, которая получает два параметра: 
название страны и название города. Функция должна возвращать одну строку в 
формате «Город, Страна» —  например, «Santiago, Chile». Сохраните функцию в 
модуле с именем city_functions.py. Создайте файл test_cities.py для 
тестирования только что написанной функции (не забудьте импортировать unittest 
и тестируемую функцию). Напишите метод test_city_country() для проверки того,
что вызов функции с такими значениями, как 'santiago' и 'chile', дает 
правильную строку. Запустите test_cities.py и убедитесь в том, что тест
test_city_country() проходит успешно.'''

import unittest
from city_function import get_city_country

class CityCountryTest(unittest.TestCase):
    
    def test_city_country(self):
        correct_info = get_city_country('madrid', 'spain')
        self.assertEqual(correct_info, 'Madrid, Spain')
if __name__ == '__main__':
    unittest.main()