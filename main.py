from time import sleep

from Physics.MotionController import MotionController
from Graphics.Bullet import Bullet
from Graphics.CanvasGraph import CanvasGraph

screen = {"width": 800, "height": 600}
x0 = 20

xmin, ymin, xmax, ymax = 0, 0, 10, 10    # world
umin, vmin, umax, vmax = 0, 480, 640, 0  # viewport (note: y reversed)

points = [(2,2), (4,4), (7,7), (8,8)]  # some "world" points


def world_to_viewport(worldpoint):
    x, y = worldpoint
    u = (x - xmin)*((umax - umin)/(xmax - xmin)) + umin
    v = (y - ymin)*((vmax - vmin)/(ymax - ymin)) + vmin
    return u, v


def pixel_to_world(pixel):
    u, v = pixel
    x = (u - umin)*((xmax - xmin)/(umax - umin)) + xmin
    y = (v - vmin)*((ymax - ymin)/(vmax - vmin)) + ymin
    return x, y


def main():
    print("Starts running here")
    motion = MotionController()
    graph = CanvasGraph(screen["width"], screen["height"])
    # bullet = Bullet(graph.canvas)
    coords = motion.trajectory_coords(45, 30, x0)

    # for y in coords:
    #     print(y)
    # exit(0)
    # self.canvas.move(self.canvas_id, self.speed, 0)
    def move():
        x = x0
        for y in coords:
            sleep(0.025)
            x = x + 1

            print(x, round(y))

            Bullet(graph.canvas, x, round(y))
            graph.canvas.update()

        # if graph.canvas.coords(bullet.canvas_id)[2] < graph.width:
        #     graph.canvas.after(10, move)

    move()
    graph.mainloop()


if __name__ == "__main__":
    main()
