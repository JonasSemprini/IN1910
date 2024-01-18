import numpy as np
import matplotlib.pyplot as plt


def vertices(v0, v1):
    """
    Function for calculating the last corner
    Arguments:
    ----------
        v0 (ndarray): First coordinate
        v1 (ndarray): Second coordinate


    Returns:
    --------
        [ndarray]: Array with three points to form a
        triangle
    """
    edge_hyp = v1[0]
    edge_kat1 = edge_hyp / 2
    h = (np.sqrt(3) / 2) * edge_hyp
    v2 = [edge_kat1, h]
    verts = np.array([v0, v1, v2])

    return verts


def linear_combinations(V, n):
    """
    Function for calculating a starting point.
    Arguments:
    ----------
        V (ndarray): List of vertices
        n (ndarray): number of iterations

    Returns:
    --------
        None, only plots
    """
    X = 0
    for _ in range(n):
        w = np.random.random(3)
        norm = w/sum(w)
        X = 0
        for i in range(0, len(w)):
            X = X + V[i] * norm[i]
        # Plots 1000 points inside the triangle with corners c
            plt.plot(X[0], X[1], "ro")

def x_halves(V, n):
    """
    Function for calculating a starting point.
    Arguments:
    ----------
        V (ndarray): List of vertices
        n (ndarray): number of iterations

    Returns:
    --------
        None, only plots with color-representation
    """
    w = np.random.random(3)
    w_list = [w[0], w[1], w[2]]
    s = sum(w_list)
    norm = [float(i)/s for i in w_list]
    X = 0
    for i in range(0, len(w)):
        X = X + V[i] * norm[i]

    X_next = np.zeros((n, 2))
    X_next[0] = np.array(X)
    colors = np.zeros(n)
    for i in range(5, n - 1):
        k = np.random.randint(3)
        X_next[i + 1] = (X_next[i] + V[k]) / 2
        colors[i + 1] = k

        red = X_next[colors == 0]
        green = X_next[colors == 1]
        blue = X_next[colors == 2]

    plt.scatter(*zip(*red), s=0.2, marker=".", color="red")
    plt.scatter(*zip(*blue), s=0.2, marker=".", color="blue")
    plt.scatter(*zip(*green), s=0.2, marker=".", color="green")


def color_map(V, n):
    """
    Function for calculating a starting point.
    Arguments:
    ----------
        V (ndarray): List of vertices
        n (ndarray): number of possible iterations

    Returns:
    --------
        None, only plots with color gradient
    """

    r0 = np.array([1, 0, 0])
    r1 = np.array([0, 1, 0])
    r2 = np.array([0, 0, 1])

    r = np.array([r0, r1, r2])

    C = np.zeros((n, 3))
    C[0] = np.array([0, 0, 0])

    X = np.zeros((n, 2))

    for i in range(1, n - 1):
        j = np.random.randint(0, 3)
        C[i + 1] = (C[i] + r[j]) / 2
        X[i + 1] = (X[i] + V[j]) / 2

    plt.axis("equal")
    plt.axis("off")

    plt.scatter(*zip(*X), c=C, s=1)

if __name__ == '__main__':

    v0 = np.array([0, 0])
    v1 = np.array([1, 0])
    V = vertices(v0, v1)
    plt.scatter(*zip(*V))
    n = 1000
    linear_combinations(V, n)
    x_halves(V, n)

    color_map(V, n)

    plt.axis('equal')
    plt.axis('off')
    plt.show()
