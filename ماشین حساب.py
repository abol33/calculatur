from tkinter import *
from tkinter.ttk import Combobox


def sum():
    num1 = float(entry_one.get())
    num2 = float(entry_two.get())
    result = num1 + num2
    label_result.configure(text=result)
def sub():
    num1 = float(entry_one.get())
    num2 = float(entry_two.get())
    result = num1 - num2
    label_result.configure(text=result)
def mult():
    num1 = float(entry_one.get())
    num2 = float(entry_two.get())
    result = num1 * num2
    label_result.configure(text=result)
def div():
    num1 = int(entry_one.get())
    num2 = int(entry_two.get())
    result = num1 / num2
    label_result.configure(text=result)

def get_ans():
    # Check errors in expression entered
    try:
        word = eval(display.get())
        display.set(word)
    except:
        word = "ERROR"
        display.set(word)

def pow():
        num1 = float(entry_one.get())
        num2 = float(entry_two.get())
        result = num1 ** num2
        label_result.configure(text=result)
def funcation_calc():
    if combo_operators.get() == '+':
        sum()
    elif combo_operators.get() == '-':
        sub()
    elif combo_operators.get() == '*':
        mult()
    elif combo_operators.get() == '/':
        div()
    elif combo_operators.get() == '**':
        pow()

form1 = Tk()

entry_one = Entry(master=form1)
entry_two = Entry(master=form1)
operators = ['+','-','*','/','**']
combo_operators = Combobox(master=form1, values=operators)
button_ok = Button(master=form1, text='=', command=funcation_calc)
label_result = Label(master=form1, text='')
eror = Label(master=form1 , text='eror')

entry_one.pack()
combo_operators.pack()
entry_two.pack()
button_ok.pack()
label_result.pack()




mainloop()