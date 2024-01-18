import numpy as np
import matplotlib.pyplot as plt
from chaos_game import ChaosGame

class Variations:
    def __init__(self, x, y, name):
        """
        Constructor that takes parameter x, y and name.

        Parameters:
        ----------

        x : list
        A list of x-values to be transformed.

        y : list
        A list of y-values to be transformed.

        name : string
        A string with the name of the transformation we want to use.
        The name has to match one of these names:
            -   linear
            -   handkerchief
            -   swirl
            -   disc
            -   heart
            -   ex
            -   hyperbolic
            -   power
            -   fisheye
        """
        self.x = x; self.y = y; self.name = name
        names = ["linear", "handkerchief", "swirl", "disc", "heart", "ex", "hyperbolic", "power", "fisheye"]
        assert name in names, "Incorrect transformation name."
        self._func = getattr(Variations, name)


    @staticmethod
    def linear(x, y):
        """
        Method for linear transformation.

        Parameters:
        ----------

        x : list
        A list of x-values to be transformed.

        y : list
        A list of y-values to be transformed.
        """
        return x, y

    @staticmethod
    def handkerchief(x, y):
        """
        Method for handkerchief transformation.

        Parameters:
        ----------

        x : list
        A list of x-values to be transformed.

        y : list
        A list of y-values to be transformed.
        """
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(y, x)
        return r*np.sin(theta+r), r*np.cos(theta - r)

    @staticmethod
    def swirl(x, y):
        """
        Method for swirl transformation.

        Parameters:
        ----------

        x : list
        A list of x-values to be transformed.

        y : list
        A list of y-values to be transformed.
        """
        r = np.sqrt(x**2 + y**2)
        return x*np.sin(r**2) - y*np.cos(r**2), x*np.cos(r**2) + y*np.sin(r**2)

    @staticmethod
    def disc(x, y):
        """
        Method for disc transformation.

        Parameters:
        ----------

        x : list
        A list of x-values to be transformed.

        y : list
        A list of y-values to be transformed.
        """
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(y, x)
        return (theta/np.pi)*np.sin(np.pi*r), (theta/np.pi)*np.cos(np.pi*r)

    @staticmethod
    def heart(x, y):
        """
        Method for heart transformation.

        Parameters:
        ----------

        x : list
        A list of x-values to be transformed.

        y : list
        A list of y-values to be transformed.
        """
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(y, x)
        return r*np.sin(theta*r), -r*np.cos(theta*r)

    @staticmethod
    def ex(x, y):
        """
        Method for ex transformation.

        Parameters:
        ----------

        x : list
        A list of x-values to be transformed.

        y : list
        A list of y-values to be transformed.
        """
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(y, x)
        p0 = np.sin(theta+r); p1 = np.cos(theta-r)
        return r*(p0**3+p1**3), r*(p0**3-p1**3)

    @staticmethod
    def hyperbolic(x, y):
        """
        Method for hyperbolic transformation.

        Parameters:
        ----------

        x : list
        A list of x-values to be transformed.

        y : list
        A list of y-values to be transformed.
        """
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(y, x)
        return np.sin(theta)/r, r*np.cos(theta)

    @staticmethod
    def power(x, y):
        """
        Method for power transformation.

        Parameters:
        ----------

        x : list
        A list of x-values to be transformed.

        y : list
        A list of y-values to be transformed.
        """
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(y, x)
        return r**(np.sin(theta))*np.cos(theta), r**(np.sin(theta))*np.sin(theta)

    @staticmethod
    def fisheye(x, y):
        """
        Method for fisheye transformation.

        Parameters:
        ----------

        x : list
        A list of x-values to be transformed.

        y : list
        A list of y-values to be transformed.
        """
        r = np.sqrt(x**2 + y**2)
        return 2/(r+1)*y, 2/(r+1)*x

    def transform(self):
        """
        Method for transforming the given x- and y-values.
        Returns a list of transformed x-values and transformed y-values
        """
        x, y = self._func(self.x, self.y)
        return x, y

    def from_chaos_game(self, instance, name):
        """
        Method for that takes an instace from ChaosGame and a transformation name,
        and returns u and v values corresponding to the transformed
        x and y values.

        Parameters:
        ----------

        instance : chaos_game.ChaosGame class object
        An instance of a ChaosGame object.

        name : string
        The name of the transformation you want to use.
        """

        x = instance.X
        var = Variations(x[:,0], -x[:,1], name)
        u, v = var.transform()
        return u, v

    def linear_combination_wrap(self, V1, V2):
        """
        Method for combining two transformations to one.

        Parameters:
        ----------

        V1 : tuple
        Tuple with the u and v values of the variation of the linear
        transformation you want to change from.

        V2 : tuple
        Tuple with the u and v values of the variation of the linear
        transformation you want to change from.
        """
        def V12(w):
            return w*V2[0] + (1-w)*V1[0], (w*V2[1] + (1-w)*V1[1])
        return V12


if __name__ == "__main__":

    """Exercise 4b)"""

    N = 100
    grid_values = np.linspace(-1, 1, N)
    x, y = np.meshgrid(grid_values, grid_values)
    x_values = x.flatten()
    y_values = y.flatten()


    transformations = ["linear", "handkerchief", "swirl", "disc", "heart", "ex", "hyperbolic", "power", "fisheye"]
    variations = [Variations(x_values, y_values, version) for version in transformations]

    fig, axs = plt.subplots(3, 3, figsize=(9, 9))
    for i, (ax, variation) in enumerate(zip(axs.flatten(), variations)):
        u, v = variation.transform()

        ax.plot(u, -v, markersize=1, marker=",", linestyle="", color="black")
        ax.set_title(variation.name)
        ax.axis("off")

    fig.savefig("figures/variations_4b.png")
    plt.show()

    """Exercise 4c)"""

    var = Variations(0,0,"linear")

    N = 100
    grid_values = np.linspace(-1, 1, N)
    x, y = np.meshgrid(grid_values, grid_values)
    x_values = x.flatten()
    y_values = y.flatten()

    transformations = ["linear", "handkerchief", "swirl", "disc", "heart", "ex", "hyperbolic", "power", "fisheye"]

    fig, axs = plt.subplots(3, 3, figsize=(9, 9))
    for i, (ax, variation) in enumerate(zip(axs.flatten(), transformations)):

        n, r = 4, 1/3
        ngon = ChaosGame(n, r)
        u, v = var.from_chaos_game(ngon, variation)

        ax.scatter(u, -v, s=0.2, marker=".", c=ngon._gradient_color())
        ax.set_title(variation)
        ax.axis("off")

    fig.savefig("figures/variations_4b.png")
    plt.show()

    """Exercise 4d)"""

    coeffs = np.linspace(0, 1, 4)

    var = Variations(0,0,"linear")
    n, r = 4, 1/3
    ngon = ChaosGame(n, r)

    V1 = var.from_chaos_game(ngon, "linear")
    V2 = var.from_chaos_game(ngon, "disc")

    variation12 = var.linear_combination_wrap(V1, V2)

    fig, axs = plt.subplots(2, 2, figsize=(9, 9))
    for ax, w in zip(axs.flatten(), coeffs):
        u, v = variation12(w)

        ax.scatter(u, -v, s=0.2, marker=".", c=ngon.gradient_color())
        ax.set_title(f"value = {w:.2f}")
        ax.axis("off")

    plt.show()
