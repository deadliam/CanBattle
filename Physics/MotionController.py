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

    def __y(self, alpha, v0, x):
        return (x * math.tan(alpha)) - ((x ** 2) * (self.g / (2 * (v0 ** 2) * (math.cos(alpha) ** 2))))

    # x0i - cannon position
    # v0 - start velocity
    # alpha - start angle
    def trajectory_coords(self, alpha, v0, x0i):
        coords = []
        for x in range(x0i, self.x1i):
            xx = (x - x0i)
            y = self.__y(alpha, v0, xx)
            if y < 0:
                break
            coords.append(y)
            # print(x, round(y))
        return coords
