import math
from tkinter import *
from Graphics.Barrel import Barrel

screen = {"width": 800, "height": 600}


class CanvasGraph:

    def __init__(self):
        self.root = Tk()
        self.root.bind('w', self.keypress)
        self.root.bind('s', self.keypress)
        # self.root.bind('a', self.keypress)
        # self.root.bind('d', self.keypress)
        self.canvas = Canvas(self.root, width=screen["width"], height=screen["height"], bg="white")
        self.canvas.pack()
        self.draw_land()
        self.barrel = Barrel(self.canvas)
        self.barrel.draw_barrel()

    def keypress(self, event):
        # print(event)
        if event.char == 'w':
            # print("UP")
            # Barrel(self.canvas, 0, -2)
            self.barrel.remove_barrel()
            self.barrel.angle -= 1
            self.barrel.draw_barrel()
        elif event.char == 's':
            # print("DOWN")
            # Barrel(self.canvas, 0, 2)
            self.barrel.remove_barrel()
            self.barrel.angle += 1
            self.barrel.draw_barrel()
        # elif event.char == 'a':
        #     # print("LEFT")
        #     Barrel(self.canvas, -2, 0)
        # elif event.char == 'd':
        #     # print("RIGHT")
        #     Barrel(self.canvas, 2, 0)
        else:
            pass

    def mainloop(self):
        self.root.mainloop()

    def draw_land(self):
        self.canvas.create_line(5, screen["height"] - 5, screen["width"] - 5, screen["height"] - 5, fill="blue")
