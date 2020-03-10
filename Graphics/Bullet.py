

class Bullet(object):

    def __init__(self, canvas, end_screen_pixels, x=10, y=10, radius=10, color="red", speed=2):
        self.end_screen_pixels = end_screen_pixels
        self.canvas = canvas
        self.speed = speed
        self.canvas_id = canvas.create_oval(x - radius, y - radius, x + radius, y + radius,
                                            outline=color, fill=color)

    def move(self):
        self.canvas.move(self.canvas_id, self.speed, 0)
        if self.canvas.coords(self.canvas_id)[2] < self.end_screen_pixels:
            self.canvas.after(10, self.move)
