
# img = tk.PhotoImage(file="mega.png")
# image = canvas.create_image(10, 10, anchor=tk.NW, image=img)


class Bullet:

    def __init__(self, canvas, x=10, y=10, radius=3, color="blue"):
        self.canvas = canvas
        self.canvas_id = canvas.create_oval(x - radius, y - radius, x + radius, y + radius,
                                            outline=color, fill=color)