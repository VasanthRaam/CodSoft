#Calculator

from tkinter import *

equation=""
def clicked(value):
    global equation
    equation = equation + str(value)
    answer.set(equation)

def calc():
    global equation
    total=str(eval(equation))
    answer.set(total)  
    equation=""
    

def clear():
    global equation
    equation=""
    answer.set("")
    
obj=Tk()
obj.title('Calculator')
obj.minsize(500,500)
answer=StringVar()
expression = Entry(obj, textvariable=answer)
expression.grid(columnspan=7, ipadx=100)

button1 = Button(obj, text=' 1 ', command=lambda: clicked(1), height=1, width=5)
button1.grid(row=2, column=0)

button2 = Button(obj, text=' 2 ',command=lambda: clicked(2), height=1, width=5)
button2.grid(row=2, column=1)
 
button3 = Button(obj, text=' 3 ', command=lambda:clicked(3), height=1, width=5)
button3.grid(row=2, column=2)

button4 = Button(obj, text=' 4 ', command=lambda:clicked(4), height=1, width=5)
button4.grid(row=2, column=3)

button5 = Button(obj, text=' 5 ', command=lambda:clicked(5), height=1, width=5)
button5.grid(row=3, column=0)

button6 = Button(obj, text=' 6 ', command=lambda:clicked(6), height=1, width=5)
button6.grid(row=3, column=1)

button7 = Button(obj, text=' 7 ', command=lambda:clicked(7), height=1, width=5)
button7.grid(row=3, column=2)

button8 = Button(obj, text=' 8 ', command=lambda:clicked(8), height=1, width=5)
button8.grid(row=3, column=3)

button9 = Button(obj, text=' 9 ', command=lambda:clicked(9), height=1, width=5)
button9.grid(row=4, column=1)

button0 = Button(obj, text=' 0 ', command=lambda:clicked(0), height=1, width=5)
button0.grid(row=4, column=2)

plus = Button(obj, text=' + ', command=lambda:clicked("+"), height=1, width=5)
plus.grid(row=7, column=0)

minus = Button(obj, text=' - ', command=lambda:clicked("-"), height=1, width=5)
minus.grid(row=7, column=1)

multiply = Button(obj, text=' * ', command=lambda:clicked("*"), height=1, width=5)
multiply.grid(row=7, column=2)

divide = Button(obj, text=' / ', command=lambda:clicked("/"), height=1, width=5)
divide.grid(row=7, column=3)
        
equal = Button(obj, text=' = ', command=calc, height=1, width=5)
equal.grid(row=9, column=2)
        
clear = Button(obj, text='Clear', command=clear, height=1, width=5)
clear.grid(row=9, column=1)

obj.configure(bg='orange')

obj.mainloop()
