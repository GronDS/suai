'''11.3. Работник: напишите класс Employee, представляющий работника. 
Метод __init__() должен получать имя, фамилию и ежегодный оклад; все эти
значения должны сохраняться в атрибутах. Напишите метод give_raise(), который
по умолчанию увеличивает ежегодный оклад на $5000 — но при этом может получать
другую величину прибавки. Напишите тестовый сценарий для Employee. Напишите два
тестовых метода, test_give_default_raise() и test_give_custom_raise(). 
Используйте метод setUp(), чтобы вам не приходилось заново создавать экземпляр
Employee в каждом тестовом метода. Запустите свой тестовый сценарий и убедитесь
в том, что оба теста прошли успешно.'''

class Employee():
    '''Presents info about employee'''
    def __init__(self, f_name, sec_name, salary):
        self.f_name = f_name
        self.sec_name = sec_name
        self.salary = salary
        
    def give_raise(self, sal_raise = 5000) :
        '''adds $5,000 to the annual salary by default but also accepts
        a different raise amount '''
        self.salary += sal_raise