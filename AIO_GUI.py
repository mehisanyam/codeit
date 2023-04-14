# In main file
# import script1
# print(script1.sum(1, 3))
# python 3.7.1

from tkinter import *

root = Tk()
root.title("ALL IN ONE")


def bmi():
    root.title("BMI")
    v = StringVar()
    d = StringVar()
    e1 = Label(root, text="WEIGHT").place(x=10, y=60)
    f1 = Entry(root, textvariable=v, justify=CENTER, cursor="plus").place(x=60, y=60)

    f2 = Entry(root, textvariable=d, justify=CENTER, cursor="plus").place(x=60, y=90)
    e2 = Label(root, text="HEIGHT").place(x=10, y=90)

    def call():
        e3 = round((float(v.get()) / float(d.get()) ** 2), 4)
        if e3 <= 18.5:
            e4 = Label(root, text=f"YOUR BMI IS:-  UNDERWEIGHT(i.e. {e3})").place(x=85, y=150)
        elif e3 < 24.9 or e3 > 18.5:
            e4 = Label(root, text=f"YOUR BMI IS:-  NORMAL WEIGHT(i.e. {e3})").place(x=85, y=150)
        elif e3 < 29.9 or e3 > 25:
            e4 = Label(root, text=f"YOUR BMI IS:-  OVERWEIGHT(i.e. {e3})").place(x=85, y=150)
        elif e3 < 34.9 or e3 > 30.0:
            e4 = Label(root, text=f"YOUR BMI IS:-  CLASS 1 OBESITY(i.e. {e3})").place(x=85, y=150)
        elif e3 < 39.9 or e3 > 35.0:
            e4 = Label(root, text=f"YOUR BMI IS:-  CLASS 2 OBESITY(i.e. {e3})").place(x=85, y=150)
        elif e3 >= 40.0:
            e4 = Label(root, text=f"YOUR BMI IS:-  CLASS 3 OBESITY(i.e. {e3})").place(x=85, y=150)

    s1 = Button(root, text="SUBMIT", activebackground="gray", command=call, cursor="arrow").place(x=30, y=120)
    s2 = Button(root, text="Exit", activebackground="gray", command=exit).place(x=30, y=160)
    root.mainloop()


def login():
    entry1 = Entry(root, width=50, cursor="plus", justify=CENTER, textvariable="entry1")
    entry2 = Entry(root, width=50, cursor="dot", justify=CENTER, show="*")
    label_1 = Label(root, text="Input")
    label_2 = Label(root, text="Password")
    c = Button(root, relief="raised", text="Submit")
    label_1.grid(row=0, column=0, sticky=E)
    label_2.grid(row=1, column=0, sticky=E)
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)
    c.grid(row=4)
    if entry1 == 1:
        print("as")
    root.mainloop()


def Calc():
    canvas1 = Canvas(root, width=300, height=300)
    canvas1.pack()

    entry1 = Entry(root)
    canvas1.create_window(210, 100, window=entry1)

    entry2 = Entry(root)
    canvas1.create_window(210, 140, window=entry2)

    entry3 = Entry(root)
    canvas1.create_window(210, 240, window=entry3)

    label0 = Label(root, text='Calculator')
    label0.config(font=('helvetica', 14))
    canvas1.create_window(150, 40, window=label0)

    label1 = Label(root, text='Type Value 1:')
    label1.config(font=('helvetica', 10))
    canvas1.create_window(100, 100, window=label1)

    label2 = Label(root, text='Type Value 2:')
    label2.config(font=('helvetica', 10))
    canvas1.create_window(100, 140, window=label2)

    label3 = Label(root, text='Result:')
    label3.config(font=('helvetica', 10))
    canvas1.create_window(100, 240, window=label3)

    def add():
        v1 = entry1.get()
        v2 = entry2.get()

        label4 = Label(root, text=float(v1) + float(v2), font=('helvetica', 10, 'bold'), bg='white')
        canvas1.create_window(210, 240, window=label4)

    buttonAdd = Button(text='+', command=add, bg='blue', fg='white', font=('helvetica', 9, 'bold'), width=5)
    canvas1.create_window(90, 190, window=buttonAdd)

    def sub():
        v1 = entry1.get()
        v2 = entry2.get()

        label5 = Label(root, text=float(v1) - float(v2), font=('helvetica', 10, 'bold'), bg='white')
        canvas1.create_window(210, 240, window=label5)

    buttonSub = Button(text='–', command=sub, bg='blue', fg='white', font=('helvetica', 9, 'bold'), width=5)
    canvas1.create_window(140, 190, window=buttonSub)

    def mul():
        v1 = entry1.get()
        v2 = entry2.get()

        label6 = Label(root, text=float(v1) * float(v2), font=('helvetica', 10, 'bold'), bg='white')
        canvas1.create_window(210, 240, window=label6)

    buttonMul = Button(text='x', command=mul, bg='blue', fg='white', font=('helvetica', 9, 'bold'), width=5)
    canvas1.create_window(190, 190, window=buttonMul)

    def div():
        v1 = entry1.get()
        v2 = entry2.get()

        label7 = Label(root, text=float(v1) / float(v2), font=('helvetica', 10, 'bold'), bg='white')
        canvas1.create_window(210, 240, window=label7)

    buttonDiv = Button(text='/', command=div, bg='blue', fg='white', font=('helvetica', 9, 'bold'), width=5)
    canvas1.create_window(240, 190, window=buttonDiv)

    root.mainloop()


def age():
    import calendar

    def showCal():
        import calendar

    def showCal():
        new_gui = Tk()

        new_gui.config(background="white")

        new_gui.title("CALENDER")

        new_gui.geometry("550x600")

        fetch_year = int(year_field.get())

        cal_content = calendar.calendar(fetch_year)

        cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold")

        cal_year.grid(row=5, column=1, padx=20)

        new_gui.mainloop()

    # Driver Code
    if __name__ == "__main__":
        gui = Tk()

        gui.config(background="white")

        gui.title("CALENDER")

        gui.geometry("250x140")

        cal = Label(gui, text="CALENDAR", bg="dark gray",
                    font=("times", 28, 'bold'))

        year = Label(gui, text="Enter Year", bg="light green")

        year_field = Entry(gui)

        Show = Button(gui, text="Show Calendar", fg="Black",
                      bg="Red", command=showCal)

        Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)

        cal.grid(row=1, column=1)

        year.grid(row=2, column=1)

        year_field.grid(row=3, column=1)

        Show.grid(row=4, column=1)

        Exit.grid(row=6, column=1)

        gui.mainloop()


def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="BMI", command=bmi)
filemenu.add_command(label="Login Page", command=login)
filemenu.add_command(label="calender", command=age)
filemenu.add_command(label="Calculator", command=Calc)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
