import sys
from tkinter import *
import random
from tkinter import messagebox

def motion_mouse(*args, **kwargs):
    """Наведение на кнопку Yes
    :param args:
    :param kwargs:
    :return:
    """

    btn_yes.place(x=random.randint(0, 500), y=random.randint(0, 300))



def no_button_click(*args, **kwargs):
    """Нажатие на кнопку No

    :param args:
    :param kwargs:
    :return:"""


    messagebox.showinfo('Вопрос', 'Спасибо, ваш голос учтён')
    sys.exit()


"""Создание параметров окна"""
root = Tk()  # инициализация ткинтера
root.geometry('600x400')
root.resizable(width=False, height=False)
root['bg'] = 'white'   # белый фон

"""Создание надписи"""
Label = Label(root, text='вы хотите увеличить зарплату?', font='Arial 20 bold', bg='white') # Создание надписи
Label.pack()

"""создание кнопки "да" """
btn_yes = Button(root, text='Да', font='Arial 20 bold')   # Создание кнопки да
btn_yes.place(x=80, y=100)   # Размещение кнопки
btn_yes.bind('<Enter>', motion_mouse)  # Enter: Указатель мыши  вошёл в пределы виджета

"""созданеие кнопки нет"""
btn_no = Button(root, text='Нет', font='Arial 20 bold')   # Создание кнопки да
btn_no.place(x=450, y=100)   # Размещение кнопки
btn_no.bind('<ButtonPress>', no_button_click)



if __name__ == '__main__':
    root.mainloop()

