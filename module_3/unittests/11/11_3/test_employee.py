'''11.3. Работник: напишите класс Employee, представляющий работника. 
Метод __init__() должен получать имя, фамилию и ежегодный оклад; все эти
значения должны сохраняться в атрибутах. Напишите метод give_raise(), который
по умолчанию увеличивает ежегодный оклад на $5000 — но при этом может получать
другую величину прибавки. Напишите тестовый сценарий для Employee. Напишите два
тестовых метода, test_give_default_raise() и test_give_custom_raise(). 
Используйте метод setUp(), чтобы вам не приходилось заново создавать экземпляр
Employee в каждом тестовом метода. Запустите свой тестовый сценарий и убедитесь
в том, что оба теста прошли успешно.'''

import unittest
from employee import Employee

class TestEmployeeRaise(unittest.TestCase):
    '''Tests for employee.py'''
    
    def setUp(self):
        '''Create the worker example'''
        self.my_employee = Employee('John', 'Von', 100000)
        self.start_value = 100000
        self.custom_values = [1000, 2000, 3000, 4000]
        
        
    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 105000)
    
    def test_give_custom_raise(self):
        for value in self.custom_values:
            self.my_employee.give_raise(value)
            self.assertEqual(self.my_employee.salary, self.start_value + value)
            self.start_value += value

if __name__ == '__main__':
    unittest.main()