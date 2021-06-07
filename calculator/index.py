from tkinter import *
import parser
from math import factorial

# exec
root = Tk()
root.title('Calculator by Imam')

#adding the input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=N+E+W+S)

i = 0
def get_variables(numb):
    global i
    display.insert(i, numb)
    i+=1

def get_operation(operation):
    global i
    length = len(operation)
    display.insert(i, operation)
    i+=length

def clear_all():
    display.delete(0, END)

def undo():
    enteri_string = display.get()
    if len(enteri_string):
        # get last value
        new_string = enteri_string[:-1]
        # delete char in display
        clear_all()
        # insert to display
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")

def calculate():
    enteri_string = display.get()
    try:
        a = parser.expr(enteri_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

def fact():
    enteri_string = display.get()
    try:
        result = factorial(int(enteri_string))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

#Code to add buttons to the Calculator
Button(root,text="1",command = lambda:get_variables(1)).grid(row=2,column=0, sticky=N+S+E+W)
Button(root,text=" 2",command = lambda :get_variables(2)).grid(row=2,column=1, sticky=N+S+E+W)
Button(root,text=" 3",command = lambda :get_variables(3)).grid(row=2,column=2, sticky=N+S+E+W)
 
Button(root,text="4",command = lambda :get_variables(4)).grid(row=3,column=0, sticky=N+S+E+W)
Button(root,text=" 5",command = lambda :get_variables(5)).grid(row=3,column=1, sticky=N+S+E+W)
Button(root,text=" 6",command = lambda :get_variables(6)).grid(row=3,column=2, sticky=N+S+E+W)
 
Button(root,text="7",command = lambda :get_variables(7)).grid(row=4,column=0, sticky=N+S+E+W)
Button(root,text=" 8",command = lambda :get_variables(8)).grid(row=4,column=1, sticky=N+S+E+W)
Button(root,text=" 9",command = lambda :get_variables(9)).grid(row=4,column=2, sticky=N+S+E+W)


#adding other buttons to the calculator
Button(root,text="AC",command=lambda :clear_all()).grid(row=5,column=0, sticky=N+S+E+W)
Button(root,text=" 0",command = lambda :get_variables(0)).grid(row=5,column=1, sticky=N+S+E+W)
Button(root,text=" .",command=lambda :get_variables(".")).grid(row=5, column=2, sticky=N+S+E+W)

Button(root,text=" +", command=lambda :get_operation("+")).grid(row=2, column=3, sticky=N+S+E+W)
Button(root,text=" -", command= lambda :get_operation("-")).grid(row=3, column=3, sticky=N+S+E+W)
Button(root,text=" *", command=lambda :get_operation("*")).grid(row=4, column=3, sticky=N+S+E+W)
Button(root,text=" /", command= lambda : get_operation("/")).grid(row=5, column=3, sticky=N+S+E+W)

# adding new operations
Button(root,text="pi",command= lambda :get_operation("*3.14")).grid(row=2,column=4, sticky=N+S+E+W)
Button(root,text="%",command= lambda :get_operation("%")).grid(row=3,column=4, sticky=N+S+E+W)
Button(root,text="(",command= lambda :get_operation("(")).grid(row=4,column=4, sticky=N+S+E+W)
Button(root,text="exp",command= lambda :get_operation("**")).grid(row=5,column=4, sticky=N+S+E+W)
 
Button(root,text="<-",command= lambda :undo()).grid(row=2,column=5, sticky=N+S+E+W)
Button(root,text="x!", command= lambda: fact()).grid(row=3,column=5, sticky=N+S+E+W)
Button(root,text=")",command= lambda :get_operation(")")).grid(row=4,column=5, sticky=N+S+E+W)
Button(root,text="^2",command= lambda :get_operation("**2")).grid(row=5,column=5, sticky=N+S+E+W)
Button(root,text="^2",command= lambda :get_operation("**2")).grid(row=5,column=5, sticky=N+S+E+W)
Button(root,text="=",command= lambda :calculate()).grid(columnspan=6, sticky=N+S+E+W)

root.mainloop()