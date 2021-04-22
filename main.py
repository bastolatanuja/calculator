from  tkinter import *

root=Tk()
#defining title of the project
root.title("simple calculator")
e=Entry(root, width=60,borderwidth=30,bg='powder blue')
e.grid(row=0,column=0,columnspan=3,padx= 10,pady = 10)

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global f_num
    global result
    result='add'
    f_num=int(first_number)
    e.delete(0,END)

def button_sub():
    first_number=e.get()
    global f_num
    global result
    result='sub'
    f_num=int(first_number)
    e.delete(0,END)

def button_mul():
    first_number=e.get()
    global f_num
    global result
    result='mul'
    f_num=int(first_number)
    e.delete(0,END)

def button_div():
    first_number=e.get()
    global f_num
    global result
    result='div'
    f_num=int(first_number)
    e.delete(0,END)
def button_percentage():
    first_number=e.get()
    global f_num
    global result
    result='percentage'
    e.delete(0,END)

def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if result=='add':
        e.insert(0,f_num+int(second_number))
    if result=='sub':
        e.insert(0, f_num - int(second_number))
    if result=='mul':
        e.insert(0, f_num * int(second_number))
    if result=='div':
        e.insert(0, f_num /int(second_number))
    if result=='percentage':
        e.insert(0,f_num%int(second_number))

button_1=Button(root,text="1",padx=65,pady=20,bg='grey',fg='purple',font=("arial",10,"bold"),command=lambda:button_click(1))
button_2=Button(root,text="2",padx=65,pady=20,bg='grey',fg='purple',font=("arial",10,"bold"),command=lambda:button_click(2))
button_3=Button(root,text="3",padx=65,pady=20,bg='grey',fg='purple',font=("arial",10,"bold"),command=lambda:button_click(3))
button_4=Button(root,text="4",padx=65,pady=20,bg='grey',fg='red',font=("arial",10,"bold"),command=lambda:button_click(4))
button_5=Button(root,text="5",padx=65,pady=20,bg='grey',fg='red',font=("arial",10,"bold"),command=lambda:button_click(5))
button_6=Button(root,text="6",padx=65,pady=20,bg='grey',fg='red',font=("arial",10,"bold"),command=lambda:button_click(6))
button_7=Button(root,text="7",padx=65,pady=20,bg='grey',fg='green',font=("arial",10,"bold"),command=lambda:button_click(7))
button_8=Button(root,text="8",padx=65,pady=20,bg='grey',fg='green',font=("arial",10,"bold"),command=lambda:button_click(8))
button_9=Button(root,text="9",padx=65,pady=20,bg='grey',fg='green',font=("arial",10,"bold"),command=lambda:button_click(9))
button_0=Button(root,text="0",padx=65,pady=20,bg='grey',fg='green',font=("arial",10,"bold"),command=lambda:button_click(0))
button_add=Button(root,text="+",padx=65,pady=20,bg='grey',fg='blue',font=("arial",10,"bold"),command=button_add)
button_sub=Button(root,text="-",padx=65,pady=20,bg='grey',fg='blue',font=("arial",10,"bold"),command=button_sub)
button_mul=Button(root,text="*",padx=65,pady=20,bg='grey',fg='blue',font=("arial",10,"bold"),command=button_mul)
button_div=Button(root,text="/",padx=65,pady=20,bg='grey',fg='blue',font=("arial",10,"bold"),command=button_div)
button_equal=Button(root,text="=",padx=65,pady=20,fg='blue',bg='black',command=button_equal)
button_clear=Button(root,text="Clear",padx=125,pady=20,bg='red',command=button_clear)
button_percentage=Button(root,text="%",padx=65,pady=20,bg='grey',fg='red',command=lambda:button_percentage)

#putting buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)

button_6.grid(row =2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=2)
button_clear.grid(row=6,column=0,columnspan=2)
button_add.grid(row=4,column=0)
button_sub.grid(row=5,column=1)
button_mul.grid(row=4,column=1)
button_div.grid(row=5,column=0)
button_equal.grid(row=5,column=2,columnspan=2)
button_percentage.grid(row=6,column=2)

root.mainloop()






