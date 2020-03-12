
# img = tk.PhotoImage(file="mega.png")
# image = canvas.create_image(10, 10, anchor=tk.NW, image=img)

from Physics.MotionController import MotionController


class Bullet:

    bullet = None

    def __init__(self, canvas, x=10, y=10, radius=3, color="blue"):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw_bullet(self, xx, yy, radius, color):
        return self.canvas.create_oval(xx - radius,
                                             yy - radius,
                                             xx + radius,
                                             yy + radius,
                                            outline=self.color, fill=color)

    def remove_bullet(self):
        self.canvas.delete(self.bullet)

    def shot(self, angle, velocity0, x0, y0):
        # x = x0
        motion = MotionController()
        coords = motion.trajectory_coords(angle, velocity0)
        bullet_prev = None
        for c in coords:
            bullet = self.draw_bullet(round(c[0]) + x0, y0 - round(c[1]), self.radius, self.color)
            if bullet_prev is not None:
                self.canvas.delete(bullet_prev)
            self.canvas.update()
            bullet_prev = bullet
