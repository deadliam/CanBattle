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
    graph.mainloop()


if __name__ == "__main__":
    main()
