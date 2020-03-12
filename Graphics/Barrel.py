import math


class Barrel:

    length = 60
    barr = None
    coords = None

    def __init__(self, canvas, angle=45, x0=20, y0=580):
        self.canvas = canvas
        self.x0 = x0
        self.y0 = y0
        self.angle = angle

    def calculate_barrel_pos(self):
        a = math.pi * self.angle / 180
        # print("angles = ", self.angle, a)
        x2 = self.length * math.sin(a)
        y2 = self.length * math.cos(a)
        return x2, self.y0 - y2

    def draw_barrel(self):
        self.coords = self.calculate_barrel_pos()
        self.barr = self.canvas.create_line(self.x0, self.y0, round(self.coords[0]), round(self.coords[1]), fill="red", width=3)
        # print(self.x0, self.y0, round(coords[0]), round(coords[1]))

    def increase_angle(self):
        self.angle = self.angle + 1

    def decrease_angle(self):
        self.angle = self.angle - 1

    def remove_barrel(self):
        self.canvas.delete(self.barr)

    # def move_barrel(self, deltax, deltay):
    #     self.canvas.move(self.move_barrel, deltax, deltay)
    #     self.canvas.after(50, self.move_barrel)
