from Physics.MotionController import MotionController
from Graphics.Bullet import Bullet
from Graphics.CanvasGraph import CanvasGraph

screen = {"width": 800, "height": 600}


def main():
    print("Starts running here")
    motion = MotionController()
    graph = CanvasGraph(screen["width"], screen["height"])
    bullet = Bullet(graph.canvas, screen["width"])
    bullet.move()

    graph.mainloop()


if __name__ == "__main__":
    main()
