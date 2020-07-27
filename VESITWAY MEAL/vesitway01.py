
from tkinter import*
from random import*
from datetime import datetime
import tkinter.messagebox
import sqlite3

conn =sqlite3.connect('vesitwaymeal.db')
c= conn.cursor()

#c.execute("CREATE TABLE Meal(Order_no int,Name text,Address text,mobile int,email text,time text,buyprice int, sellprice int, profit int)")

#c.execute("drop table Meal")


global x, orders, getname, getaddress, order_number, m, var,buyprice,sellprice,profit
x = int((random() * 10000))
orders = []
times = []
getname = []
getaddress = []
buyprice=[]
sellprice=[]
profit=[]

def Order():
    def ordernow():
        global getname, getaddress, m
        try:
            getname.append(entername.get())
            getaddress.append(enteraddress.get())
            getmob = str(entermob.get())
            getmail = entermail.get()
            getprice1 = buyprice.get()
            getprice2 = sellprice.get()
            if (getname == "" or getaddress == "" or getmob == "" or getmail == ""):
                tkinter.messagebox.showinfo("Empty Field", "Any Field can't be EMPTY\n")
                order.destroy()

            elif (len(getmob)>10 or len(getmob)<10):
                tkinter.messagebox.showinfo("Mob No.","Enter Valid MOBILE NO.\nExact 10 Numbers")
                order.destroy()

            else:
                global times, x, orders
                now = (datetime.now())
                d = str(
                    str(now.hour) + ":" + str(now.minute) + "::" + str(now.second) + " on " + str(now.day) + "/" + str(
                        now.month) + "/" + str(now.year))
                times.append(d)
                x += 1
                string = "Your order id is: " + str(x)
                tkinter.messagebox.showinfo("Order Placed", string)
                orders.append(x)
                i = (len(getname) - 1)
                make_list = [x, getname[i], getaddress[i], getmob, getmail, d,getprice1, getprice2, int(getprice2)-int(getprice1)]
                c.execute("INSERT INTO MEAL VALUES(?,?,?,?,?,?,?,?,?)", make_list)
                conn.commit()
                order.destroy()
        except NameError or ValueError or UnboundLocalError:
            tkinter.messagebox.showerror("Error", "Please enter valid credentials")
            order.destroy()

    order = Tk()
    global var
    var = IntVar()

    order_w = Label(order, text="ORDER FOOD", bg="black", fg="white")
    order_w.grid(row=0, column=2)

    label_a = Label(order, text="  ")
    label_a.grid(row=1)

    name = Label(order, text="Name:  ")
    name.grid(row=2, column=1)

    entername = Entry(order, bd=3)
    entername.grid(row=2, column=2)

    address = Label(order, text="Address:   ")
    address.grid(row=3, column=1)

    enteraddress = Entry(order, bd=3)
    enteraddress.grid(row=3, column=2)

    buy_price = Label(order, text="buy_price :  ")
    buy_price.grid(row=4, column=1)

    buyprice = Entry(order, bd=3)
    buyprice.grid(row=4, column=2)

    buyprice.delete(0, END)
    buyprice.insert(0, 85)

    list_value2 = Label(order, text="SMALL (85) / MEDIUM (175) / LARGE (265)")
    list_value2.grid(row=4, column=3)

    selling_price = Label(order, text="selling price :  ")
    selling_price.grid(row=5, column=1)

    sellprice = Entry(order, bd=3)
    sellprice.grid(row=5, column=2)

    sellprice.delete(0, END)
    sellprice.insert(0, 95)

    list_value2 = Label(order, text="SMALL (95) / MEDIUM (195) / LARGE (295)")
    list_value2.grid(row=5, column=3)

    mobile = Label(order, text="Mobile no:      ")
    mobile.grid(row=6, column=1)

    entermob = Entry(order, bd=3)
    entermob.grid(row=6, column=2)

    email = Label(order, text="Email id:      ")
    email.grid(row=7, column=1)

    entermail = Entry(order, bd=3)
    entermail.grid(row=7, column=2)

    label_a = Label(order, text="  ")
    label_a.grid(row=8)

    label_a = Label(order, text="  ")
    label_a.grid(row=9)

    order_now = Button(order, text="Order Now", bg="yellow", fg="blue", command=ordernow)
    order_now.grid(row=10, column=2)
    show = Button(order, text="show", bg="yellow", fg="blue", command=NewMealOrder)
    show.grid(row=10, column=3)

    label_a = Label(order, text="  ")
    label_a.grid(row=11)

    label_a = Label(order, text="  ")
    label_a.grid(column=4)

    order.mainloop()


def NewMealOrder():
    global orders, times
    new_orders = Tk()
    t = Text(new_orders, height=15, width=100)
    t.pack()
    s = "\n                  RECENT ORDERS\n\nORDER NO    NAME     ADDRESS     TIME \n"
    t.insert(END, s)
    i = 0
    for i in range(len(orders)):
        string = str(orders[i]) + "    " + str(getname[i]) + "   " + str(getaddress[i])+ "    " + str(times[i]) + "  "  +"\n"
        t.insert(END, string)

    t2 = Text(new_orders, height=18, width=100)
    t2.pack()
    t2.insert(END, "                    ALL ORDERS\n")
    t2.insert(END, "\nID,  NAME, ADDRESS, MOBILE, EMAIL, TIME/DATE, ACTUAL PRICE, SELL PRICE, PROFIT\n")

    for row in c.execute('select * from MEAL'):
        t2.insert(END, row)
        t2.insert(END, "\n")
    conn.commit()
    new_orders.mainloop()


window = Tk()

logo = PhotoImage(file="logo.gif")
order_count = IntVar()

label_a = Label(window, text="         ")
label_a.grid(column=0, row=0)

label_a = Label(window, text="   ")
label_a.grid(column=0,row=1)


def count():
    dataCopy = c.execute("select count(*) from MEAL")
    order_count = dataCopy.fetchone()
    print(order_count[0])

    identry = Label(window, text=order_count, width=10, fg='dark green', font=('Ariel', 14))
    identry.grid(column=1, row=2)


button_m1 = Button(window, text="ORDER COUNT", bg="light green", relief="raised", command=count)
button_m1.grid(row=2, column=0)

'''
label_a = Label(window, text="ORDER COUNT : ")
label_a.grid(column=0, row=2)

dataCopy = c.execute("select count(*) from MEAL")
order_count = dataCopy.fetchone()
print(order_count[0])

identry = Label(window, text=order_count, width=10,fg='dark green',font=('Ariel', 14))
identry.grid(column=1, row=2)
'''

def totprofit():
    dataCopy = c.execute("select sum(profit) from MEAL")
    total_profit = dataCopy.fetchone()
    print(total_profit[0])

    identry = Label(window, text=total_profit, width=10, fg="dark green", font=('Ariel', 14))
    identry.grid(column=1, row=4)


button_m1 = Button(window, text="TOTAL PROFIT", bg="light green", relief="raised", command=totprofit)
button_m1.grid(row=4, column=0)

'''
label_a = Label(window, text="TOTAL PROFIT : ")
label_a.grid(column=0, row=3)

dataCopy = c.execute("select sum(profit) from MEAL")
total_profit = dataCopy.fetchone()
print(total_profit[0])

identry = Label(window, text=total_profit, width=10,fg="dark green",font=('Ariel', 14))
identry.grid(column=1, row=3)
'''

label_a = Label(window, text="         ", compound=CENTER,image=logo)
label_a.grid(column=0, row=0)

button_m1 = Button(window, text=" VESITWAY FOOD", bg="light green", height="4", width="15", relief="raised",command=Order)
button_m1.grid(row=0, column=1)

label_a = Label(window, text="  ")
label_a.grid(column=2)

label_a = Label(window, text="  ")
label_a.grid(column=0,row=3)

label_a = Label(window, text="   ")
label_a.grid(column=4)

def about():
    tkinter.messagebox.showinfo("ABOUT :", "\nROLL NO |      FULL NAME     |   PHONE NO.  |\n    14          Kartik Chindarkar    9727635365\n    18            Nikhil Gaikwad      9653412755 \n    53            Gaurav Parwani       8552010984\n    69              Yuvraj Singh         9969565101")


button_m1 = Button(window, text="ABOUT", bg="light green", relief="raised", command=about)
button_m1.grid(row=6, column=0)


window.mainloop()
conn.close()
