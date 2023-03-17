from tkinter_ import *
def display_info():
    n = name.get()
    a = age.get()
    e = education.get()
    print("работает!!!")
    window.config(bg="black")

    info.insert(0, f"{a} -летний {n} закончил {e} образование")
"""Зададим конфигурацию окна"""
window = tk()
window.title("Первое знакомство с Tkinter")
window.geometry("500x300")
window.config(bg="#0f4b6e")
window.resizable(0, 0)

"""Добавим три метки и три текстовых поля"""
name_lab = Label(window, text="Введите имя", bg="#af006d", fg="#ffffff")


age_lab = Label(window, text="Введите возраст", bg="#af006d", fg="#ffffff")


education_lab = Label(window, text="Введите образование", bg="#af006d", fg="#ffffff")


name = Entry(window)
age = Entry(window)
education = Entry(window)

name_lab.pack()
#
name.place(x=200, y=250)

age_lab.pack()
age.pack()

education_lab.pack()
education.pack()

"""добавим кнопку"""
btn = Button(window, text="да", bg="#aa0000", fg="#ffffff", command=display_info, font=("Arial"))
btn.config(width=25, height=2)
btn.pack(pady=15)

info = Entry(window, width=30, font=("Arial", 14), bg="#aaaa66")
info.pack(pady=5)
# это последняя строка

window.mainloop()
