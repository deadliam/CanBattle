from time import sleep

from Physics.MotionController import MotionController
from Graphics.Bullet import Bullet
from Graphics.CanvasGraph import CanvasGraph

screen = {"width": 800, "height": 600}
x0 = 20
y0 = 580
delta_Y = 580


def main():
    print("Starts running here")
    motion = MotionController()
    graph = CanvasGraph(screen["width"], screen["height"])
    coords = motion.trajectory_coords(45, 60, x0)

    def move():
        x = x0
        for y in coords:
            # sleep(0.025)
            x = x + 1

            print(x, y - (2 * y) + delta_Y)

            Bullet(graph.canvas, x, y + 200)
            graph.canvas.update()

        # if graph.canvas.coords(bullet.canvas_id)[2] < graph.width:
        #     graph.canvas.after(10, move)

    move()
    graph.mainloop()


if __name__ == "__main__":
    main()
