
# img = tk.PhotoImage(file="mega.png")
# image = canvas.create_image(10, 10, anchor=tk.NW, image=img)

from time import sleep


class Bullet(object):

    def __init__(self, canvas, x=10, y=10, radius=10, color="red", speed=2):
        self.canvas = canvas
        self.speed = speed
        self.canvas_id = canvas.create_oval(x - radius, y - radius, x + radius, y + radius,
                                            outline=color, fill=color)

    # def move(self, coords):
    #     # self.canvas.move(self.canvas_id, self.speed, 0)
    #     x = 0
    #     for y in coords:
    #         sleep(0.025)
    #         x = x + 1
    #         self.canvas.coords(self.canvas_id, x, y, 0, 0)
    #         self.canvas.update()
    #
    #     if self.canvas.coords(self.canvas_id)[2] < self.end_screen_pixels:
    #         self.canvas.after(10, self.move)