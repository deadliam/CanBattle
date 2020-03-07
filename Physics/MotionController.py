import math
import time


class MotionController:

    # acceleration of gravity
    g = 10
    # end of the field in pixels
    x1i = 1000

    def __init__(self):
        pass

    def y(self, x: int, alpha: int, v0: int):
        return (x * math.tan(alpha)) - ((x ** 2) * (self.g / (2 * (v0 ** 2) * (math.cos(alpha) ** 2))))

    # x0i - cannon position
    # v0 - start velosity
    # alpha - start angle
    def motion(self, alpha: int, v0: int, x0i: int):
        for x in range(x0i, self.x1i):
            xx = (x - x0i)
            y = self.y(xx, alpha, v0)
            if y < 0:
                break
            print(x, round(y))

# bullet = MotionController()
# bullet.motion(45, 50, 0, 1000)
