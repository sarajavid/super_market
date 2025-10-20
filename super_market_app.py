from tkinter import *
from tkinter import messagebox
from super_market_module import *

def save():
    pass

def total():
    pass

window = Tk()
# window.config(background="black")
window.title("Product App")
window.geometry("300x330")

# Id
Label(window, text="Id").place(x=20,y=20)
id = IntVar()
Entry(window,textvariable=id).place(x=100, y =20)

# Name
Label(window, text="Name").place(x=20,y=60)
name = StringVar()
Entry(window,textvariable=name).place(x=100, y =60)

# Brand
Label(window, text="Brand").place(x=20, y=100)
brand = StringVar()
Entry(window,textvariable=brand).place(x=100, y =100)

# Quantity
Label(window, text="Quantity").place(x=20,y=140)
quantity = IntVar()
Entry(window,textvariable=quantity).place(x=100, y =140)

# Price
Label(window, text="Price").place(x=20,y=180)
price = IntVar()
Entry(window,textvariable=price).place(x=100, y =180)

# Expire_date
Label(window, text="Expire date").place(x=20,y=220)
expire_date = StringVar()
Entry(window,textvariable=expire_date).place(x=100, y =220)



Button(window,text="Save",command=save).place(x=20, y = 280, width=80)
Button(window,text="Total",command=total).place(x=145, y = 280, width=80)

window.mainloop()