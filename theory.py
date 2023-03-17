# Name = 'Zakhar' # присвоение имени
# age = 14
# print('Меня зовут', Name,'Мне',age,' лет')
# print(f'Меня зовут {Name} мне {age} лет')
# # условия
# '''много
# строчный
# комментарий'''
#
#
# a = -2
# if a < 0:
#     print(f'число {a} отрицательное')
# else:
#     print(f'число {a} положительное ')
# # print(b.lower()) #Приведение строки к нижнему регистру
"""Коллекции"""
# names = ['Vasia',  'Petya', 'Artem']
# print(names[0])
# print(names)
# names[1] = 'Ruslan'
# print(names)
#
# age = list()
# age.append('eleven')
# print(age)
#
# names.insert(1, 'Gena')
# print(names)
#
# del names[2]
# print(names)
#
# names.append('Petya')
# print(names)
#
# deleted = names.pop(2)
# print(deleted)
# print(names)
#
# names.remove('Gena')
# print(names)
# names = ['Vasya',  'Petya', 'Artem']

'''циклы'''
# for name in names:
#     if name == 'Artem':
#         continue
#     #  break
#     print(name)
# grade = 2
# while grade < 10:
#     print(f'Снова {grade}???? Наказан!')
#     grade += 1
'''функции'''
# def light_edit(action='Включили'):
#     for i in range(1, 6):
#         print(f'{action} {i} лампу')

# light_edit(action='включили')
# light_edit(action='выключили')
"""Задание"""
# b = int(input("введите число:"))
#
# if b < 0:
#     print("число отрицательное")
# elif b > -1 and b < 10:
#     print("число однозначное")
# elif b > 9 and b < 100:
#     print("число двузначное")
# elif b > 99 and b < 1000:
#     print("число трёхзначное")
# elif b > 999:
#     print("число слишком большое")
"""ООП - классы"""
# class Dog:
#     """"модель собаки"""
#     def __init__(self, name, age):
#         """Инициализация отрибутов name, age"""
#         self.name = name
#         self.age = age
# def __str__(self):
#     return f'Имя: {self.name}, возраст: {self.age}'



# some_dog = Dog(name='Шарик', age=10)
# print(some_dog.age)
# print(some_dog.name)
# some_dog_2 = ('Бобик', 8)
# print(some_dog_2)
# class Car:
"""Простая модель автомобиля"""

#     def __init__(self, brand, model, year, color):

#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.color = color
#
#
#
#     def get_description(self):
#         """Описание автомобиля"""
#         description = f'{self.brand} | {self.model} | {self.color} | {self.year}'
#         return description
#
#
#
#
# some_car = Car(brand='OPEL', model='astra', year=2007, color='silver')
# print(some_car.get_description())

"""tkinter Canvas"""

from tkinter import *

root = Tk()
root.title('canvas')
root.geometry('400x400')

canvas = Canvas(bg='white', width=250, height=250)
canvas.pack(anchor=CENTER, expand=True)
"""Создание линий"""
# canvas.create_line(10, 10, 10, 100, activefill='yellow', width=10, dash=1)
# canvas.create_line(50, 10, 50, 100, activefill='yellow', width=10, dash=1)
"""Создание прямоугольников"""
canvas.create_rectangle(10, 20, 200, 60, fill='yellow', outline='#ffffff')

root.mainloop()
