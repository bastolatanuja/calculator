from  tkinter import *

root=Tk()
#defining title of the project
root.title("simple calculator")
val=" "
data=StringVar()
e=Entry(root,bd=29, textvariable=data,justify='right',font=("aerial",25,"bold"),bg='powder blue')
e.grid(row=0,column=0,columnspan=3,padx= 10,pady = 10)


def button_click(number):
    global val
    val=val+str(number)
    data.set(val)


def button_clear():
    global val
    val=" "
    data.set("")


def button_equal():
    global val
    result=str(eval(val))
    data.set(result)

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
button_add=Button(root,text="+",padx=65,pady=20,bg='grey',fg='blue',font=("arial",10,"bold"),command=lambda:button_click("+"))
button_sub=Button(root,text="-",padx=65,pady=20,bg='grey',fg='blue',font=("arial",10,"bold"),command=lambda:button_click("-"))
button_mul=Button(root,text="*",padx=65,pady=20,bg='grey',fg='blue',font=("arial",10,"bold"),command=lambda:button_click("*"))
button_div=Button(root,text="/",padx=65,pady=20,bg='grey',fg='blue',font=("arial",10,"bold"),command=lambda:button_click("/"))
button_equal=Button(root,text="=",padx=65,pady=20,fg='blue',bg='black',command=button_equal)
button_clear=Button(root,text="Clear",padx=125,pady=20,bg='red',command=button_clear)
button_percentage=Button(root,text="%",padx=65,pady=20,bg='grey',fg='red',command=lambda:button_click("%"))

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






