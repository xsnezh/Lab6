from tkinter import *
from tkinter.ttk import Combobox

def btn_click():
    mark = 0
 #Питання №1
    if v1.get() == 1 and v2.get() == 0 and v3.get() == 1 and v4.get() == 0:
        mark += 2
    elif v1.get() == 0 and v2.get() == 0 and v3.get() == 1 and v4.get() == 0:
        mark += 1
    elif v1.get() == 1 and v2.get() == 0 and v3.get() == 0 and v4.get() == 0:
        mark += 1
    elif v1.get() == 0 and v2.get() == 0 and v3.get() == 0 and v4.get() == 0:
        mark += 0
#Питання № 2
    if v5.get() == 2:
        mark += 2
#Питання № 3
    if v7.get() == 1:
        mark += 2
#Питання № 4
    if entry.get() == 'Східній':
        mark += 2
#Питання 5
    if cb.get() == 'Харків':
        mark +=2
#Питання 6
    if scale.get() == 6:
        mark += 2
    if mark > 6:
        lbl5["fg"] = "green"
    else:
        lbl5["fg"] = "red"
    v6.set("Ваша оцінка: "+str(mark))

tk = Tk()



tk.title("Тест з Географії")
font_title = ("Times new Roman", 12, "bold")
font_q = ("Times new Roman", 11, "italic")

window = tk
window.config(bg='#ACE1AF',

              highlightcolor='#7FFF00',
              highlightthickness=3)

#Питання №1
lbl1 = Label(tk, text="Питання №1", font=font_title)
lbl2 = Label(tk, text="Якими морями омиваєтья кримський півострів?", font=font_q)
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
chb1 = Checkbutton(tk, text="Азовським", variable=v1, onvalue=1, offvalue=0)
chb2 = Checkbutton(tk, text="Червоним", variable=v2, onvalue=1, offvalue=0)
chb3 = Checkbutton(tk, text="Чорним", variable=v3, onvalue=1, offvalue=0)
chb4 = Checkbutton(tk, text="Середземним", variable=v4, onvalue=1, offvalue=0)
#Питання №2
lbl3 = Label(tk, text="Питання №2", font=font_title)
lbl4 = Label(tk, text="Як називається найвища точка Карпат?", font=font_q)
v5 = IntVar()
rbt1 = Radiobutton(tk, text="Еверест", variable=v5, value=1)
rbt2 = Radiobutton(tk, text="Говерла", variable=v5, value=2)
rbt3 = Radiobutton(tk, text="Кіліманджаро", variable=v5, value=3)
rbt4 = Radiobutton(tk, text="Піп Іван", variable=v5, value=4)
#Питання №3
lbl6 = Label(tk, text="Питання №3", font=font_title)
lbl7 = Label(tk, text="Слово Географія в перекладі з грецької означає...", font=font_q)
v7 = IntVar()
rbt5 = Radiobutton(tk, text="Землеопис", variable=v7, value=1)
rbt6 = Radiobutton(tk, text="Землеустрій", variable=v7, value=2)
rbt7 = Radiobutton(tk, text="Вивчення землі", variable=v7, value=3)
#Питання №4
lbl8 = Label(tk, text="Питання №4", font=font_title)
lbl9 = Label(tk, text="В якій частині Європи знаходиться Україна?.", font=font_q)
entry = Entry(tk, width = 30, font = "ubuntu 14",  bd=5,)
#Питання №5
lbl10 = Label(tk, text="Питання №5", font=font_title)
lbl11 = Label(tk, text="Місто-мільйонник серед запропонованих...", font=font_q)
text_variante=('Харків' ,
               'Одеса',
               'Чернігів',
               'Хмельницький')

cb=Combobox(tk, values=text_variante)
#Питання №6
lbl12 = Label(tk, text="Питання №6", font=font_title)
lbl13= Label(tk, text="Скільки материків у світі?", font=font_q)

def getV(tk):
    a = scale.get()
    print("Отримане значення: ", a)

scale = Scale(tk, orient=HORIZONTAL, length=300, from_= 0, to = 10, tickinterval=5,
               resolution=1)

btn = Button(tk, text="Відповісти", command=btn_click, font=font_q)
v6 = StringVar()
lbl5 = Label(tk, text='', textvariable=v6, font=font_title)

lbl1.pack()
lbl2.pack()
chb1.pack()
chb2.pack()
chb3.pack()
chb4.pack()
lbl3.pack()
lbl4.pack()
rbt1.pack()
rbt2.pack()
rbt3.pack()
rbt4.pack()
lbl6.pack()
lbl7.pack()
rbt5.pack()
rbt6.pack()
rbt7.pack()
lbl8.pack()
lbl9.pack()
entry.pack()
lbl10.pack()
lbl11.pack()
cb.pack()
lbl12.pack()
lbl13.pack()
scale.pack()
btn.pack()
lbl5.pack()
tk.mainloop()

