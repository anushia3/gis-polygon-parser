import matplotlib.pyplot as plt


def plot_polygon(vertices):
    x = [point[0] for point in vertices]
    y = [point[1] for point in vertices]

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, marker="o")

    plt.axis("equal")
    plt.grid(True)

    plt.show()
