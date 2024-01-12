from typing import List, TypeVar
from dataclasses import dataclass

T = TypeVar("T")


class Array:
    data: List
    size: int = 0
    capacity: int = 0
    type: T

    def __init__(self, type: T, size: int = 0) -> None:
        self.type = type
        self.data = [type] * size
        self.size = size
        self.counter = 0
    
    def __len__(self):
        return self.size    
        
        
    def __iter__(self):
        self.counter = 0
        return self
    
    def __next__(self):
        if self.counter + 1 <= self.size:
            self.counter+= 1
            return self.data[self.counter - 1]
        else:
            raise StopIteration

    def __str__(self):
        return f"{self.data}"

    def __getitem__(self, key: int) -> T:
        return self.data[key]

    def __setitem__(self, key: int, value: T):
        try:
            if type(value) == self.type:
                self.data[key] = value
            else:
                raise ValueError('Incorrect type')
        except ValueError as error:
            print(error)
            raise
        
    def __contains__(self, item: int) -> bool:
        if item in self.data:
            return True
        else:
            return False

        
    def __reversed__(self) -> List:
        # self.data = self.data[::-1]
        return self.data[::-1]
    

    
if __name__ == "__main__":
    arr: Array = Array(int, 5)
    print(arr)
    arr[3] = 6
    print(arr)
    print(6 in arr)
    print(reversed(arr))
    for i in arr:
        print(i)
    