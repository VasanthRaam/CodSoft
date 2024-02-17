from tkinter import *
import random


window = Tk()
window.title("Password Generator")
window.minsize(width=500,height=500)
window.config(padx=50,pady=100)

pass_variables = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$',
                  '%', '&', '*', '+']

def Mybutton():
   length=int(text1.get())
   pass_list = []
   for i in range(length):
       pass_list.append(random.choice(pass_variables))
   random.shuffle(pass_list)
   password = ""
   for i in pass_list:
       password+=i
   text2.config(text=password)
   
text1=Entry()
text1.grid(column=1,row=0)

label2=Label(text="Enter the Length of Password")
label2.grid(column=2,row=0)

label3=Label(text="Password")
label3.grid(column=0,row=3)

text2=Label(text="0")
text2.grid(column=1,row=3)

button1=Button(text="Generate",command=Mybutton)
button1.grid(column=2,row=4)

window.mainloop()

