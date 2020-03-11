from tkinter import *


class CanvasGraph:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.canvas = Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack()

    def mainloop(self):
        self.root.mainloop()
