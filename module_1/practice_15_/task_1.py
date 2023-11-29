'''Есть список из 10 случайных чисел. Напишите программу, которая делит эти
числа на пары кортежей внутри списка, и выведите результат на экран.
Дополнительно: решите задачу несколькими способами.'''

original_list: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list: list = []

# counter: int = 1
# for number in range(0,len(original_list),2):
#     new_list.append(tuple((original_list[number], original_list[counter])))
#     counter+= 2
# print(new_list)

new_list: list = list(zip(original_list[::2], original_list[1::2]))
print(new_list)