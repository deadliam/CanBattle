from tkinter import *


class CanvasGraph:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.canvas = Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack()

        # self.ball = self.c.create_oval(0, 500, 40, 140, fill='green')

    # def motion(self):
    #     self.c.move(self.ball, 1, 0)
    #     if self.c.coords(self.ball)[2] < 300:
    #         self.root.after(10, self.motion)

    def mainloop(self):
        self.root.mainloop()
