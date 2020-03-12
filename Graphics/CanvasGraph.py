import math
import time

from tkinter import *
from Graphics.Barrel import Barrel
from Graphics.Bullet import Bullet

screen = {"width": 800, "height": 600}


class CanvasGraph:

    current_angle = 45
    velocity0 = 60

    def __init__(self):
        self.root = Tk()
        self.root.bind('w', self.keypress)
        self.root.bind('s', self.keypress)
        self.root.bind('a', self.keypress)
        self.root.bind('d', self.keypress)
        self.root.bind('r', self.keypress)

        self.label1 = Label(text="Angle: " + str(self.current_angle), fg="#eee", bg="#333")
        self.label2 = Label(text="Velocity: " + str(self.velocity0), fg="#eee", bg="#333")
        self.label1.pack()
        self.label2.pack()

        # self.angle_label = Label(self.root, textvariable=self.l1).pack()
        # self.velocity_label = Label(self.root, textvariable=self.l2).pack()
        self.canvas = Canvas(self.root, width=screen["width"], height=screen["height"], bg="white")
        self.canvas.pack()
        self.draw_land()
        self.barrel = Barrel(self.canvas)
        self.barrel.draw_barrel()
        self.bullet = Bullet(self.canvas)


    def keypress(self, event):
        # print(event)
        if event.char == 'w':
            self.bullet.remove_bullet()
            self.barrel.remove_barrel()
            self.barrel.angle -= 1
            self.current_angle = 90 - self.barrel.angle
            self.barrel.draw_barrel()
        elif event.char == 's':
            self.bullet.remove_bullet()
            self.barrel.remove_barrel()
            self.barrel.angle += 1
            self.current_angle = 90 - self.barrel.angle
            self.barrel.draw_barrel()
        elif event.char == 'r':
            # self.bullet.remove_bullet()
            self.bullet.shot(self.current_angle, self.velocity0, self.barrel.coords[0], self.barrel.coords[1])
            self.clear_all_and_draw_world()

        elif event.char == 'a':
            self.velocity0 -= 2
        elif event.char == 'd':
            self.velocity0 += 2
        else:
            pass
        print(self.current_angle, self.velocity0)
        self.label1.configure(text="Angle: " + str(self.current_angle))
        self.label2.configure(text="Velocity: " + str(self.velocity0))

    def clear_all_and_draw_world(self):
        self.canvas.delete("all")
        self.draw_land()
        self.barrel.draw_barrel()

    def mainloop(self):
        self.root.mainloop()

    def draw_land(self):
        self.canvas.create_line(5, screen["height"] - 5, screen["width"] - 5, screen["height"] - 5, fill="blue")
