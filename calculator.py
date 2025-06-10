from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("313x400")
window.resizable(False, False)

entry = Entry(window, width=16, font=('Arial', 24), borderwidth=2, relief='ridge')
entry.grid(row=0, column=0, columnspan=4)

result_shown = False

def click(number):
    current = entry.get()

    global result_shown
    if result_shown:
        if isinstance(number, int):  # if digit pressed after result
            entry.delete(0, END)
            entry.insert(END, str(number))
            result_shown = False
        else:
            result_shown = False
    elif isinstance(number, int):
        entry.insert(END, str(number))
    else:
        if current.endswith(('+', '-', '*', '/')) and number in ('+', '-', '*', '/'):
            entry.delete(len(current)-1, END)
        entry.insert(END, str(number))

def calculate():
    global result_shown
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")
    result_shown = True

button_1 = Button(window, text='1', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=lambda: click(1))
button_2 = Button(window, text='2', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=lambda: click(2))
button_3 = Button(window, text='3', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=lambda: click(3))
button_4 = Button(window, text='4', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=lambda: click(4))
button_5 = Button(window, text='5', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=lambda: click(5))
button_6 = Button(window, text='6', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=lambda: click(6))
button_7 = Button(window, text='7', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=lambda: click(7))
button_8 = Button(window, text='8', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=lambda: click(8))
button_9 = Button(window, text='9', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=lambda: click(9))
button_0 = Button(window, text='0', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=lambda: click(0))
button_add = Button(window, text='+', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=lambda: click('+'))
button_subtract = Button(window, text='-', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=lambda: click('-'))
button_multiply = Button(window, text='*', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=lambda: click('*'))
button_divide = Button(window, text='/', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=lambda: click('/'))
button_equal = Button(window, text='=', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE)
button_clear = Button(window, text='C', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=lambda: entry.delete(0, END))
button_backspace = Button(window, text='←', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=lambda: entry.delete(len(entry.get())-1, END))
button_equal = Button(window, text='=', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=calculate)
button_plus_minus = Button(window, text='±', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE,state=DISABLED)
button_dot = Button(window, text='.', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE, command=lambda: click('.'))
button_percent = Button(window, text='%', width=5, height=2, font=('Arial', 18),bd=1, relief=GROOVE,state=DISABLED)

button_clear.grid(row=1, column=0)
button_backspace.grid(row=1, column=1)
button_plus_minus.grid(row=1, column=2)
button_divide.grid(row=1, column=3)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)
button_percent.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_dot.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

window.mainloop()