from tkinter import *
import tkinter

# ========================= Setting ==========================
root = Tk()
root.geometry('400x200')
root.title('Calculator')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)

# ========================= Variables ==========================
num1 = StringVar()
num2 = StringVar()
res_val = StringVar()

# ========================= Frames ==========================
top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg=color)
top_forth.pack(side=TOP)


# ========================= Functions ==========================
def errorMsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error', 'Somthing went wrong')
    elif ms == 'division zero error':
        tkinter.messagebox.showerror('Division Error', 'Can not Divide by 0')


def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        res_val.set(value)
    except:
        errorMsg('error')


def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        res_val.set(value)
    except:
        errorMsg('error')


def mul():
    try:
        value = float(num1.get()) * float(num2.get())
        res_val.set(value)
    except:
        errorMsg('error')


def div():
    if num2.get() == '0':
        errorMsg('division zero error')
    elif num2.get() != '0':
        try:
            value = float(num1.get()) / float(num2.get())
            res_val.set(value)
        except:
            errorMsg('error for division function')


# ========================= Buttons ==========================
btn_plus = Button(top_third, text="+", width=10, highlightbackground=color, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=10, pady=10)

btn_minus = Button(top_third, text="-", width=10, highlightbackground=color, command=lambda: minus())
btn_minus.pack(side=LEFT, padx=10, pady=10)

btn_mul = Button(top_third, text="*", width=10, highlightbackground=color, command=lambda: mul())
btn_mul.pack(side=LEFT, padx=10, pady=10)

btn_div = Button(top_third, text="/", width=10, highlightbackground=color, command=lambda: div())
btn_div.pack(side=LEFT, padx=10, pady=10)

# ========================= Entries and Lable ==========================
lable_first_num = Label(top_first, text='input number 1: ', bg=color)
lable_first_num.pack(side=LEFT, padx=10, pady=10)

first_num = Entry(top_first, highlightbackground=color, textvariable=num1)
first_num.pack(side=LEFT)

lable_second_num = Label(top_second, text='input number 2: ', bg=color)
lable_second_num.pack(side=LEFT, padx=10, pady=10)

secon_num = Entry(top_second, highlightbackground=color, textvariable=num2)
secon_num.pack(side=LEFT)

res = Label(top_forth, text='Result: ', bg=color)
res.pack(side=LEFT, padx=10, pady=10)

res_num = Entry(top_forth, highlightbackground=color, textvariable=res_val)
res_num.pack(side=LEFT)

root.mainloop()