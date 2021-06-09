from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

# function
def addBook():
    global inputIdBook, inputTitleBook, inputAuthorBook, inputStatusBook, cur, con, tableBook, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=600)
    root.geometry("400x600")

    # connect to DB
    pwd = ''
    db = 'library-db'
    tableBook = 'books'

    con = pymysql.connect(host='localhost', user="root", database=db, password=pwd)
    cur = con.cursor()

    # create bg to frame
    canvas1 = Canvas(root)
    canvas1.config(bg="green")
    canvas1.pack(expand=True, fill=BOTH) #expand -> fullscreen

    # add heading
    headingFr1 = Frame(root, bg="blue", bd=5)
    headingFr1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFr1, text="Add Book", bg="black", fg="white")
    headingLabel.place(relx=0, rely=0.1, relwidth=1, relheight=0.3)

    # add area to input data book
    inputFrame = Frame(root, bg="black", bd=3)
    inputFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # id book
    # labelIDBook = Label(inputFrame, text="Book ID", bg="black", fg="white")
    # labelIDBook.place(relx=0.05, rely=0.2, relheight=0.08)
    # inputIdBook = Entry(inputFrame)
    # inputIdBook.place(relx=0.3, rely=0.2, relwidth=0.6, relheight=0.08)

    # titleBook
    labelTitleBook = Label(inputFrame, text="Title Book", bg='black', fg='white')
    labelTitleBook.place(relx=0.05, rely=0.35, relheight=0.08)
    inputTitleBook = Entry(inputFrame)
    inputTitleBook.place(relx=0.3, rely=0.35, relwidth=0.6, relheight=0.08)

    # authorBook
    labelAuthorBook = Label(inputFrame, text="Author Book", bg='black', fg='white')
    labelAuthorBook.place(relx=0.05, rely=0.5, relheight=0.08)
    inputAuthorBook = Entry(inputFrame)
    inputAuthorBook.place(relx=0.3, rely=0.5, relwidth=0.6, relheight=0.08)

    # statusBook
    labelStatusBook = Label(inputFrame, text="Status(Available/issued) : ", bg='black', fg='white')
    labelStatusBook.place(relx=0.05, rely=0.65, relheight=0.08)
    inputStatusBook = Entry(inputFrame)
    inputStatusBook.place(relx=0.3, rely=0.65, relwidth=0.6, relheight=0.08)

    # Button 
    buttonSave = Button(inputFrame, text="Save", bg='blue', fg='black', command=regBook)
    buttonSave.place(relx=0.05, rely=0.8, relwidth=0.87, relheight=0.08)

    # quit
    buttonQuit = Button(inputFrame, text="Back to Home", bg="green", fg="black", command=root.destroy)
    buttonQuit.place(relx=0.05, rely=0.9, relwidth=0.87, relheight=0.08)
    

    root.mainloop()


def regBook():
    # idBook = inputIdBook.get()
    titleBook = inputTitleBook.get()
    authorBook = inputStatusBook.get()
    statusBook = inputStatusBook.get()
    statusBook = statusBook.lower()

    # insert book to DB
    insertBook = "insert into "+tableBook+"  (bid, title, author, status) values ('', '"+titleBook+"','"+authorBook+"','"+statusBook+"');"

    print(insertBook)

    # exec
    try:
        cur.execute(insertBook)
        con.commit()
        messagebox.showinfo('Success', 'Book added successfully')
    except:
        messagebox.showinfo('Error', "Can't add data to Database")

    
    # print(idBook)
    print(titleBook)
    print(authorBook)
    print(statusBook)