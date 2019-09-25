from tkinter import *
import pyodbc

#run when button is clikced
def callback():
    #get user inputs from textbox
    s=e1.get()
    q=e2.get()
    #connect to sql database
    conn = pyodbc.connect(DataBase Connection)
    cursor = conn.cursor()
    #Sql insert query
    cursor.execute("""insert into Database
                       (Columns Name) values (?,?)""",(s,q))
    conn.commit()
    conn.close()
    #print results
    print(s,q)
    print('Data Inserted')


#create GUI with 2 text box and submit button
master = Tk() 
Label(master, text='First Name').grid(row=0) 
Label(master, text='Last Name').grid(row=1) 
e1 = Entry(master) 
e2 = Entry(master) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
MyButton1 = Button(master, text="Submit", width=10, command=callback)
MyButton1.grid(row=2, column=1)

mainloop() 
