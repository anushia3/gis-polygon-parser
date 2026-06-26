import matplotlib.pyplot as plt


def plot_polygon(vertices, show=True):
    x = [point[0] for point in vertices]
    y = [point[1] for point in vertices]

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.plot(x, y, marker="o")

    ax.set_aspect("equal")
    ax.grid(True)

    if show:
        plt.show()

    return fig