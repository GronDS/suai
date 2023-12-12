while True:
    try:
        number_n :int= int(input('Введите число N: '))
        if number_n > 0:
            break
        if type(number_n) != int:
            raise TypeError
        # ('Неверный ввод, число должно быть целым и больше 0!')
        if number_n < 0:
            raise ValueError('Число должно быть больше 0!')
    except (TypeError, ValueError) as error:
        print(error)
        continue
        
class Squares():
    # Class generate squares from 1 to number_n
    def __init__(self) -> None:
        self.__limit = number_n
        self.__counter = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__counter <= self.__limit:
            answer = self.__counter ** 2
            self.__counter += 1
            return f'===\n{self.__counter - 1} ** 2 = {answer}'
        else:
            raise StopIteration
        
iter_1 = Squares()

for square in iter_1:
    print(square)