from typing import List, TypeVar
from dataclasses import dataclass


T = TypeVar("T")


class DynamicArray:
    data: List
    type: T

    def __init__(self, type: T) -> None:
        self.type = type
        self.size = 0
        self.capacity = 1
        
        self.data = self.make_array(self.capacity)
        
        self.counter = 0
    
    def __len__(self):
        return self.size    
        
        
    def __iter__(self):
        self.counter = 0
        return self
    
    def __next__(self) -> List|StopIteration:
        if self.counter + 1 <= len(self.data):
            self.counter+= 1
            return self.data[self.counter - 1]
        else:
            raise StopIteration

    def __str__(self):
        return f"{self.data}"

    def __getitem__(self, key: int) -> T:
        try:
            if 0 <= key <= self.size:
                return self.data[key]
            else:
                raise IndexError('key index is out of range')
        except IndexError as error:
            print(error)
            raise
        
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
        return self.data[::-1]
    
    def _resize(self, new_cap): 
        new_data = self.make_array(new_cap)  # New bigger array
 
        for k in range(self.size):  # Reference all existing values
            new_data[k] = self.data[k]
 
        self.data = new_data  # Call A the new bigger array
        self.capacity = new_cap  # Reset the capacity
    
    def append(self, ele):
        if self.size == self.capacity:
            self._resize(self.capacity + 1)

        self.data[self.size] = ele  # Set self.n index to element
        self.size += 1
        
    def make_array(self, new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return ([self.type] * new_cap)
    def sum(self) -> T|TypeError:
        summable_types = [int, float, bool]
        
        try:
            summ = 0
            if self.type in summable_types:
                for i in self.data:
                    summ += i
                return summ
            else:
                raise TypeError(f'{self.type} is unsummable type!')
        except TypeError as error:
            print(error)
            raise
        
    def average(self) -> float|TypeError:
        try:
            if self.sum != TypeError:        
                return self.sum() / self.size
            else:
                raise TypeError(f'{self.type} is unsummable type!')
        except TypeError as error:
            print(error)
            raise
        
    
if __name__ == "__main__":
    arr: DynamicArray = DynamicArray(int)
    arr.append(9)
    arr.append(8)
    arr.append(7)
    arr.append(6)
    arr.append(5)
    arr.append(4)
    print(arr)
    print('len', len(arr))
    print(arr[0])
    print(arr[1])
    arr[3] = 11
    print(arr)
    print(reversed(arr))
    print(11 in arr)
    print(12 in arr)
    print(arr.sum())
    print(arr.average())
    
    arr: DynamicArray = DynamicArray(bool)
    arr.append(True)
    arr.append(False)
    arr.append(False)
    arr.append(False)
    arr.append(True)
    print(arr.sum())
    print(arr.average())