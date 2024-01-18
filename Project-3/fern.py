import matplotlib.pyplot as plt
import numpy as np


class Affinetransform:
    """
    ==============================================
    Class Affinetransform to solve and plot different
    kinds of tranformations
    ==============================================
    """

    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        """
        Constructs all necessary attributes for the f object
        Arguments:
        ----------
            a, b, c, d, e, f (float): All floats numbers, positive
            and negative
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self, x, y):
        """
        Special method computing the differential equation
        Arguments:
        ----------
            x (int): x-position for starting point
            y (int): y-position for starting point

        Returns:
        --------
            [ndarray]: Starting point for our transformation.
        """
        a, b, c, d, e, f = self.a, self.b, self.c, self.d, self.e, self.f;
        fourmatrix = np.array([[a, b], [c, d]])
        points = np.array([x, y])
        twomatrix = np.array([e, f])
        point = fourmatrix @ points + twomatrix

        self.pass_point = point
        return point


def choose(p_values, functions):
    """
    Method choosing which function to pass further on.
    Arguments:
    ----------
        p_values (ndarray): List with values, 0 < p < 1
        functions (int): list with differnt kind of
        functions

    Returns:
    --------
        [ndarray]: Chosen function due to probability.
    """
    r = np.random.random()
    p_cumulative = np.cumsum(p_values)
    for j, p in enumerate(p_cumulative):
        if r < p:
            return functions[j]

def iterate(steps, discard, functions):
    """
    Method iterating several times our choose method to
    obtain values.
    Arguments:
    ----------
        steps (int): Number of iterations
        functions (int): List with differnt kind of
        functions

    Returns:
    --------
        [ndarray]: Many positional values due to
        probability.
    """
    X = [[0, 0]]
    X_prev = [0, 0]

    for i in range(1, steps + discard):
        a, b, c, d, e, f = choose(p_values, functions)
        F = Affinetransform(a, b, c, d, e, f)
        X_prev = F(X_prev[0], X_prev[1])
        X.append(X_prev)
    X = np.array(X)
    return X[discard:]

if __name__ == '__main__':

    f1 = [0, 0, 0, 0.16, 0, 0]
    f2 = [0.85, 0.04, -0.04, 0.85, 0, 1.60]
    f3 = [0.20, -0.26, 0.23, 0.22, 0, 1.60]
    f4 = [-0.15, 0.28, 0.26, 0.24, 0, 0.44]

    functions = [f1, f2, f3, f4]
    p_values = [0.01, 0.85, 0.07, 0.07]

    steps = 50000
    discard = 5
    X = iterate(steps, discard, functions)
    plt.axis('equal')
    plt.axis('off')
    plt.scatter(*zip(*X), s=0.1, marker=".", color= "forestgreen")
    plt.savefig("figures/barnsley_fern.png")
    plt.show()
