import math
import time
from tkinter import *
from Graphics.Bullet import Bullet


class MotionController:

    # acceleration of gravity
    g = 10
    # end of the field in pixels
    x1i = 1000

    def __init__(self):
        pass

    def y(self, x, alpha, v0):
        return (x * math.tan(alpha)) - ((x ** 2) * (self.g / (2 * (v0 ** 2) * (math.cos(alpha) ** 2))))

    # x0i - cannon position
    # v0 - start velocity
    # alpha - start angle
    def motion(self, alpha, v0, x0i):
        for x in range(x0i, self.x1i):
            xx = (x - x0i)
            y = self.y(xx, alpha, v0)
            if y < 0:
                break
            print(x, round(y))
            # self.window.draw_bullet(xx, y + 100)
