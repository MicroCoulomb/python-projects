from tkinter import *

# button
def calculate():
    miles = float(entry.get())
    km = round(miles * 1.60934, 2)
    km_value.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(200, 100)
window.config(padx=20, pady=20)

# input
entry = Entry(width=10)
entry.grid(row=0, column=1)

# label
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.config(padx=10)
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to", font=("Arial", 12))
equal_label.grid(row=1, column=0)

km_value = Label(text="0", font=("Arial", 12, "bold"))
km_value.grid(row=1, column=1)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)



window.mainloop()