#!/bin/python3
from tkinter import *
from PIL import ImageGrab, ImageTk

root = Tk()
root.wm_attributes("-topmost", 1)
canvas = Canvas(root, width=400, height=400)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

def ins():
    im = ImageGrab.grabclipboard()
    if im:
        image = ImageTk.PhotoImage(im)
        canvas.create_image(0, 0, anchor=NW, image=image)
        canvas.image = image

Button(root, text="Insert", command=ins).pack(side=LEFT)
root.mainloop()
