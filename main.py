from tkinter import *
import sqlite3
from tkinter import messagebox

window=Tk()
window.title("family dhaba")
window.geometry("700x500")

#conn = sqlite3.connect("family_dhaba_database.db")
#c = conn.cursor()
#c.execute("CREATE TABLE orderdetails (name TEXT, aloo_paratha INT, samosa INT, tea INT, fried_rice INT)")
#conn.commit()
#conn.close()

def calculate():
    aloo_paratha=e1.get()
    samosa=e2.get()
    tea=e3.get()
    fried_rice=e4.get()


    total=((int(aloo_paratha)*30)+(int(samosa)*5)+(int(fried_rice)*35)+(int(tea)*10))
    label12=Label(window,text= total,font="times 18")
    label12.place(x=100,y=360)
    print(total)

def submitorder():
    aloo_paratha = e1.get()
    samosa = e2.get()
    tea = e3.get()
    fried_rice = e4.get()
    name = e5.get()

    conn = sqlite3.connect("family_dhaba_database.db")
    c = conn.cursor()
    c.execute("INSERT INTO orderdetails VALUES('"+name+"',"+aloo_paratha+","+samosa+","+tea+","+fried_rice+")")
    messagebox.showinfo("Your order is placed please wait...")
    conn.commit()
    conn.close()

def orderdetailsofcustomers():
    root=Tk()
    root.title("Order Details Records")
    root.geometry("700x500")
    label=Label(root, text="Order Details Records", font = "time 15 bold", bg="blue", fg="white", padx=250, pady=10)
    label.grid(row = 0, column = 0, columnspan=20)

    p1=Label(root, text="Name", font="time 10 bold")
    p1.grid(row=1, column=0, padx =10, pady=10)

    p2 = Label(root, text="Aloo_paratha", font="time 10 bold")
    p2.grid(row=1, column=4, padx=10, pady=10)

    p3 = Label(root, text="Samosa", font="time 10 bold")
    p3.grid(row=1, column=5, padx=10, pady=10)

    p4 = Label(root, text="Tea", font="time 10 bold")
    p4.grid(row=1, column=6, padx=10, pady=10)

    p5 = Label(root, text="Fried_rice", font="time 10 bold")
    p5.grid(row=1, column=7, padx=10, pady=10)

    conn = sqlite3.connect("family_dhaba_database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM orderdetails")
    r=c.fetchall()
    num = 2
    for i in r:
        name=Label(root, text=i[0], font ="time 8 bold", fg="blue")
        name.grid(row=num, column=0, padx=10, pady=10)

        aloo_paratha=Label(root, text=i[1], font="time 8 bold", fg="blue")
        aloo_paratha.grid(row=num, column=4, padx=10, pady=10)

        samosa=Label(root, text=i[2], font="time 8 bold", fg="blue")
        samosa.grid(row=num, column=5, padx=10, pady=10)

        tea=Label(root, text=i[2], font="time 8 bold", fg="blue")
        tea.grid(row=num, column=6, padx=10, pady=10)

        fried_rice=Label(root, text=i[2], font="time 8 bold", fg="blue")
        fried_rice.grid(row=num, column=7, padx=10, pady=10)

        num=num+1

    conn.commit()
    conn.close()




label1=Label(window,text="MENU",font="times 28 bold")
label1.place(x=550,y=70)

label2=Label(window,text="aloo paratha        Rs.30",font="times 18")
label2.place(x=450,y=120)

label3=Label(window,text="samosa                Rs.5",font="times 18")
label3.place(x=450,y=150)

label4=Label(window,text="fried rice             Rs.35",font="times 18")
label4.place(x=450,y=180)

label5=Label(window,text="tea                       Rs.10",font="times 18")
label5.place(x=450,y=210)

label6=Label(window,text="Family Dhaba",fg="Red",font="times 28 bold")
label6.place(x=350,y=20,anchor="center")

label7=Label(window,text="Select the items",font="times 21 bold")
label7.place(x=70,y=70)

label8=Label(window,text="aloo paratha",font="times 18")
label8.place(x=20,y=120)

e1=Entry(window)
e1.place(x=20,y=150)

label9=Label(window,text="samosa",font="times 18")
label9.place(x=250,y=120)

e2=Entry(window)
e2.place(x=250,y=150)

label10=Label(window,text="tea",font="times 18")
label10.place(x=20,y=200)

e3=Entry(window)
e3.place(x=20,y=230)

label11=Label(window,text="fried rice",font="times 18")
label11.place(x=250,y=200)

label13=Label(window,text="Total Bill",font="times 18")
label13.place(x=0,y=360)

label14=Label(window,text="Enter your Name",font="times 18")
label14.place(x=0,y=420)

e4=Entry(window)
e4.place(x=250,y=230)

e5=Entry(window)
e5.place(x=180,y=430)

b2=Button(window,text="bill",font = "time 10 bold",width=20,bg="blue", fg="white",command=calculate)
b2.place(x=100,y=300)

b3=Button(window,text="Submit Order",font = "time 10 bold",width=30,bg="blue", fg="white",command=submitorder)
b3.place(x=380,y=380)

b3=Button(window,text="Owner Options",font = "time 10 bold",width=30,bg="blue", fg="white",command=orderdetailsofcustomers)
b3.place(x=380,y=440)



window.mainloop()