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

def get_city_country(city, country, population=''):
    '''Generate a neatly formatted city info.'''
    if population:
        city_info = f'{city.title()}, {country.title()} —  population {population}'
    else:
        city_info = f'{city.title()}, {country.title()}'
    return city_info