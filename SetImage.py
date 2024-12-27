from tkinter import *
from PIL import Image,ImageTk


def set_background(root, image_path):
    # Open the image file
    image_0 = Image.open(image_path)
    # Convert the image for Tkinter
    bck_img = ImageTk.PhotoImage(image_0)
    # Set the geometry of the root window (optional)
    # root.geometry("1200x710")
    # Create a label with the image
    imagelbl = Label(root, image=bck_img)
    # Place the label to cover the entire root window
    imagelbl.place(relheight=1, relwidth=1)
    # Keep a reference to the image to prevent garbage collection
    imagelbl.image = bck_img