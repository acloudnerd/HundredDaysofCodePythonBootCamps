from tkinter import *
from PIL import Image, ImageTk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT_TUPLE = (FONT_NAME, 50, "bold")

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Lufuno-ro")
window.config(padx=100, pady=10, bg=PINK)
window.resizable(False, False)

title_label = Label(text="Timer", fg=RED, font=(FONT_NAME, 50, "bold"), bg=PINK)
title_label.grid(column=1, row=0)

CANVAS_W, CANVAS_H = 200, 250

canvas = Canvas(width=CANVAS_W, height=CANVAS_H, bg=PINK, highlightthickness=0)
pil_img = Image.open("baby_lufuno_bg_removed.png").resize((CANVAS_W, CANVAS_H)).convert("RGBA")
background = Image.new("RGBA", (CANVAS_W, CANVAS_H), PINK)
background.paste(pil_img, mask=pil_img.split()[3])
lufuno_img = ImageTk.PhotoImage(background.convert("RGB"))
canvas.create_image(CANVAS_W // 2, CANVAS_H // 2, image=lufuno_img)
canvas.create_text(CANVAS_W // 2, CANVAS_H // 2 + 50, text="00:00", font=FONT_TUPLE, fill=RED)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, )
start_button.grid(column=0, row=1)
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=1)

check_marks = Label(text="✔️", fg=GREEN, bg=PINK, highlightthickness=0)
check_marks.grid(column=1, row=2)


window.mainloop()