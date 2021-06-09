from tkinter import *
from PIL import ImageTk, Image 
import pymysql
from tkinter import messagebox
from AddBook import *
from ViewBooks import *
from DeleteBook import *
from IssueBook import *

# connect to db
pwd = ''
db = 'library-db'
con = pymysql.connect(host="localhost", user="root", password=pwd, database=db)
cur = con.cursor()
print(cur)

# create window
root = Tk()
root.title = 'Library by Imam'
root.minsize(width=400, height=600)
root.geometry("600x1000")

# create head frame
headingFrm1 = Frame(root, bg="green", bd=5)
headingFrm1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrm1, text='Welcome to Library', bg='black', fg='white')
headingLabel.place(relx=0, rely=0, relheight=1, relwidth=1)

# create add button
btnA = Button(root, text="Add Book", bg='black', fg='white', command=addBook)
btnA.place(relx=0.1, rely=0.4, relwidth=0.4, relheight=0.1)

btnB = Button(root, text="Delete Book", bg='black', fg='white', command=delete)
btnB.place(relx=0.1, rely=0.5, relwidth=0.4, relheight=0.1)

btnC = Button(root, text="View Book List", bg='black', fg='white', command=view)
btnC.place(relx=0.1, rely=0.6, relwidth=0.4, relheight=0.1)

btnD = Button(root, text="Issue Book to Student", bg='black', fg='white', command=issueBook)
btnD.place(relx=0.1, rely=0.7, relwidth=0.4, relheight=0.1)

root.mainloop()
