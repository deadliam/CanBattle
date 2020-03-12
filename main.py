from time import sleep
from Graphics.Barrel import Barrel
from Physics.MotionController import MotionController
from Graphics.Bullet import Bullet
from Graphics.CanvasGraph import CanvasGraph


x0 = 20
y0 = 580
delta_Y = 580


def main():
    print("Starts running here")
    graph = CanvasGraph()

    motion = MotionController()
    coords = motion.trajectory_coords(45, 60, x0)

    # def move():
    #     x = x0
    #     # for y in coords:
    #     for y in range(50, 100):
    #         sleep(1.025)
    #         x = x + 1
    #         # print(x, -y + delta_Y)
    #         # Bullet(graph.canvas, x, -y + delta_Y)
    #         Barrel(graph.canvas, x, y)
    #         graph.canvas.update()
    # move()


    graph.mainloop()


if __name__ == "__main__":
    main()
