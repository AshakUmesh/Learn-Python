from tkinter import *


def miles_to_km_convert():
    miles = input_text.get()
    km = float(miles) * 1.60934
    output_label["text"] = km


window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)


input_text = Entry(width=10)
input_text.grid(row=0, column=1)


miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)


equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)


output_label = Label(text="0")
output_label.grid(row=1, column=1)


km_label = Label(text="Km")
km_label.grid(row=1, column=2)


button = Button(text="Calculate", command=miles_to_km_convert)
button.grid(row=2, column=1)

window.mainloop()