from tkinter import *
from PIL import Image, ImageTk

# constants
CANVAS_W, CANVAS_H = 200, 200
PINK = "#e2979c"


# creating the window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.resizable(False, False)

# setting up and showing the canvas
canvas = Canvas(width=CANVAS_W, height=CANVAS_H)

pil_image = Image.open("logo.png").resize((CANVAS_W, CANVAS_H)).convert("RGBA")
background = Image.new("RGBA", (CANVAS_W, CANVAS_H), PINK)
background.paste(pil_image, mask=pil_image.split()[3])
logo_img = ImageTk.PhotoImage(background.convert("RGB"))
canvas.create_image(CANVAS_W // 2, CANVAS_H // 2, image=logo_img)
canvas.grid(column=1, row=1)


window.mainloop()