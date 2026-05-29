import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# labelling

my_label = tkinter.Label(text="I am a label", font=("Arial", 34, "italic"))

my_label.pack(expand=1)



window.mainloop()
