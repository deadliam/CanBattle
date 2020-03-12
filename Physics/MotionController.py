import math
from time import sleep


class MotionController:

    # acceleration of gravity
    g = 10
    # end of the field in pixels
    x1i = 800

    def __init__(self):
        pass

    def trajectory_coords(self, alpha, v0):
        coords = []
        t = 0
        for i in range(1000):
            # sleep(0.01)
            t += 0.02
            x = t * v0 * math.cos(math.radians(alpha))
            y = v0 * math.sin(math.radians(alpha)) * t - (self.g / 2) * t * t
            if y < -80:
                break
            coords.append([x, y])

        return coords