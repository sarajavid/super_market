from tkinter import *
from tkinter import messagebox
from super_market_module import *


def save():
    try:
        name_validator(name.get())
        brand_validator(brand.get())
        quantity_validator(quantity.get())
        price_validator(price.get())
        expire_date_ = expire_date_validator(expire_date.get())

        product = {
            "id": id.get(),
            "name": name.get(),
            "brand": brand.get(),
            "quantity": quantity.get(),
            "price": price.get(),
            "expire": expire_date_,
        }
        product_list.append(product)
        messagebox.showinfo("Saved", "Person saved successfully")
        id.set(0)
        name.set("")
        brand.set("")
        quantity.set(0)
        price.set(0)
        expire_date.set(str(date.today()))

    except Exception as e:
        messagebox.showerror("Save Error", f"Error : {e}")


def get_total():
    total = 0
    for product in product_list:
        total += product["quantity"] * product["price"]

    messagebox.showinfo("Total", f"Total Price : {total}")


window = Tk()
# window.config(background="black")
window.title("Product App")
window.geometry("300x330")

# Id
Label(window, text="Id").place(x=20, y=20)
id = IntVar()
Entry(window, textvariable=id).place(x=100, y=20)

# Name
Label(window, text="Name").place(x=20, y=60)
name = StringVar()
Entry(window, textvariable=name).place(x=100, y=60)

# Brand
Label(window, text="Brand").place(x=20, y=100)
brand = StringVar()
Entry(window, textvariable=brand).place(x=100, y=100)

# Quantity
Label(window, text="Quantity").place(x=20, y=140)
quantity = IntVar()
Entry(window, textvariable=quantity).place(x=100, y=140)

# Price
Label(window, text="Price").place(x=20, y=180)
price = IntVar()
Entry(window, textvariable=price).place(x=100, y=180)

# Expire_date
Label(window, text="Expire date").place(x=20, y=220)
Label(window, text="(yyyy-mm-dd)").place(x=100, y=240)
expire_date = StringVar()
Entry(window, textvariable=expire_date).place(x=100, y=220)

Button(window, text="Save", command=save).place(x=20, y=280, width=80)
Button(window, text="Total", command=get_total).place(x=145, y=280, width=80)

window.mainloop()
