from tkinter import *
from tkinter import ttk


# Create window object
app = Tk()
app.title("Noemnkaltura xisoblash")
app.geometry("800x300")


def show():
    k = float(kenglik.get())
    u = float(uzoqlik.get())
    m = masshtab.get()
    if m == "1:1000 000":
        print("1:1000000")
    

    title = Label(app, text="Siz kiritgan ma`lumotlar",  font=("bold", 16), pady=10, padx=10)
    title.grid(row=0, column=4)

    k_label = Label(app, text=f"Kenglik: {k}",  font=("bold", 14), pady=10, padx=10)
    k_label.grid(row=1, column=3)
    y_label = Label(app, text=f"Uzqolik {u}",  font=("bold", 14), pady=10, padx=10)
    y_label.grid(row=2, column=3)




# Header
app_title = Label(app, text="Koordinatalarni kiriting",
                  font=("bold", 16), pady=10, padx=10)
app_title.grid(row=0, column=0)

# Kenglik label
kenglik_label = Label(app, text="Kenglik", font=("bold", 14), padx=10, pady=5)
kenglik_label.grid(row=1, column=0, sticky=W)
# Kenglik label
kenglik = StringVar()
kenglik_form = Entry(app, textvariable=kenglik)
kenglik_form.grid(row=1, column=1, sticky=W)

# Uzoqlik label
uzoqlik_label = Label(app, text="Uzqolik", font=("bold", 14), padx=10, pady=5)
uzoqlik_label.grid(row=2, column=0, sticky=W)
# Uzoqlik label
uzoqlik = StringVar()
uzoqlik_form = Entry(app, textvariable=uzoqlik)
uzoqlik_form.grid(row=2, column=1, sticky=W)

# Select
masshtab = StringVar()

masshtab_label = Label(app, text="Masshtab tanlang",
                       font=("bold", 14), padx=10, pady=5)
masshtab_label.grid(row=3, column=0, sticky=W)

# Masshtab select form
masshtab_form = ttk.Combobox(app, width=17, textvariable=masshtab)
masshtab_form.grid(row=3, column=1, sticky=W)
masshtab_form['values'] = ["1:1000 000",
                           "1:500 000",
                           "1:300 000"]
masshtab_form.current(0)

# form
button = Button(app, text="Xisoblash", command=show, padx=5, pady=5, width=15)
button.grid(row=4, column=1)


# Start programm
app.mainloop()
