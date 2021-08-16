import numpy as np
import matplotlib.pyplot as plt


class VectorVisualizer:
    def __init__(self) -> None:
        self.colorlist = ["r", "g", "b", "c", "m", "y"]

    def plot_2d(self, vector):
        vec_size = np.shape(vector)
        if not vec_size[1] == 2:
            print("vector shpae must be (,2)")
            print("your vector in plot2D pucton is :", vec_size)
            return 1
        origin = np.zeros((2, vec_size[0]))
        plt.quiver(
            *origin,
            vector[:, 0],
            vector[:, 1],
            color=self.colorlist[: vec_size[0]],
            scale=21
        )
        plt.show()


def main():
    print("test for visualizer")
    V = np.array([[1, 1], [-2, 2], [10, 10]])
    vec_vis = VectorVisualizer()
    vec_vis.plot_2d(V)

    # origin = np.array([[0, 0, 0],[0, 0, 0]]) # origin point
    # plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=21)
    # plt.show()


if __name__ is "__main__":
    main()
else:
    main()
