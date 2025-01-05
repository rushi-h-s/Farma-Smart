from tkinter import *
from PIL import Image, ImageTk

class BackgroundPage:
    def __init__(self, root):
        self.root = root
        # ensure that size of image is same as/greater than size of frame
        self.f = Frame(root, width=1600, height=900)
        self.f.pack()
        self.f.pack_propagate(0)

        self.raw_image = Image.open("Complex Frame.png")
        # define the size of the image, which will also determine the size of the button
        self.raw_image = self.raw_image.resize((1600, 900))
        self.img = ImageTk.PhotoImage(self.raw_image)

        self.panel = Label(self.f, image=self.img)
        self.panel.pack()
        self.f.pack_propagate(0)
        self.panel.pack_propagate(0)


if __name__ == "__main__":
    root = Tk()
    d = BackgroundPage(root)
    root.mainloop()







"""
The file which is executed, uska __name__ ==> "__main__"
All the other file which are not executed, uska __name__ ==> "filename"
"""
