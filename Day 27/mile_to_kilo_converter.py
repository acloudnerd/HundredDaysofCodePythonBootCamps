from tkinter import * 

window = Tk()
window.title("Your little converter buddy")
window.minsize(height=500, width=500)

entry = Entry(width=10)
entry.grid(row=0,column=3)

def calculator():
    miles = entry.get()
    kilos = int(miles)*1.60934
    result = Label(text=kilos, font=("Arial", 34, "italic"))
    result.pack(expand=1)

kilo_button = Button(text="Click me to convert", command=calculator)
kilo_button.grid(row=1,column=3)



window.mainloop()