from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

# connect DB
pwd = ''
DB = 'library-db'
conn = pymysql.connect(host='localhost', user="root", database=DB, password=pwd)
cur = conn.cursor()

# def view():
root = Tk()
root.title('Library')
root.minsize(width=800, height=600)
root.geometry('800x600')

canvas2 = Canvas(root)
canvas2.config(bg="green")
canvas2.pack(expand=True, fill=BOTH)

# content heading 
headingFrame = Frame(root, bg='blue', bd=5)
headingFrame.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.1)

headingLabel = Label(headingFrame, text="View Books", bg='black', fg='white')
headingLabel.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)

# content label list
labelFrame = Frame(root, bg='black', bd=5)
labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.5)
Label(labelFrame, text="%-10s%-40s%-30s%-20s"%('BID','Title','Author','Status'), bg='black',fg='white').place(relx=0.07,rely=0.1)
Label(labelFrame, text = "----------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)

# getting data books
bookTbl = 'books'
getData = "select * from "+bookTbl
cur.execute(getData)
conn.commit()

for i in cur:
    print(i)

root.mainloop()