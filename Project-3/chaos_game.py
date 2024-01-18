import matplotlib.pyplot as plt
import numpy as np


class ChaosGame:
    """
    ==============================================
    Class ChaosGame implemented to express,
    and solve different fractal systems.
    ==============================================
    """
    def __init__(self, n, r):
        """
        Constructs all necessary attributes for the f object
        Arguments:
        ----------
            r (float): Step towards vertices
            n (int): number of vertices
            self._generate_ngon(): Call to generate vertices of a n-gon.
        """
        self.r = r
        if (isinstance(n, int) and (n >= 3)):
            self.n = n
        else:
            raise ValueError("Needs to be int type and not smaller than 3!")

        if (isinstance(r, float) and (r < 1 and r > 0)):
            self.r = r
        else:
            raise ValueError("Needs to be float type and between 0 and 1!")

        self._generate_ngon()

    def _generate_ngon(self):
        """
        Private method computing the n-gon

        Variables:
        ----------
            theta (scalars): intial interval values
            c_marked (ndarray): Array to store vertices
        Returns:
        --------
            None, only stores the calculated theta and c_marked values
            for potential further usage
        """
        theta = np.linspace(0, 2 * np.pi, self.n, endpoint=False)
        c_marked = np.zeros((len(theta), 2))
        for j in range(0, self.n):
            c_marked[j][0] = np.sin(theta[j])
            c_marked[j][1] = np.cos(theta[j])
        self._theta = theta
        self._c_marked = c_marked

    def _starting_point(self):
        """
        Private method computing the starting point

        Variables:
        ----------
            n (int): number of vertices
            w (ndarray): Array for random values in intervall 0 <= w < 1
            norm(ndarray): array w normalized
        Returns:
        --------
            None, only stores the calculated starting point
        """
        n = self.n
        w = np.random.random(n)
        norm = w/sum(w)

        self.X_start = [0, 0]
        for i in range(0, len(w)):
            self.X_start = (self.X_start + self._c_marked[i] * norm[i])

        self.X = self.X_start

    def iterate(self, steps, discard=5):
        """
        Method computing several points inside our n-gon
        with a specialized formula.

        Arguments:
        ----------
            steps (int): number of iterations
            discard (int): number of ignored points at start

        Variables:
        ----------
            n (int): number of vertices
            X_next (ndarray): Array for calculated values
            colors(ndarray): Array that memorizes an integer
            associated with a calculated point
        Returns:
        --------
            None, only stores the calculated points and color array
        """
        x0 = self.X
        X_next = np.zeros((steps + discard, 2))
        X_next[0] = np.array(x0)
        colors = np.zeros(steps + discard)

        for i in range(0, steps + (discard - 1)):
            k = np.random.randint(self.n)
            corner = self._c_marked[k]
            X_next[i + 1] = self.r * X_next[i] + (1 - self.r) * corner
            colors[i + 1] = k
        self.steps = steps
        self.X_next = X_next[discard:]
        self.colors = colors[discard:]

    def plot_ngon(self):
        """
        Method for plotting our n-gon.

        Variables:
        ----------
            f (instance): instance for our calculated vertices

        Returns:
        --------
            None, only plots
        """
        f = self._c_marked
        plt.axis('equal')
        plt.axis('off')
        #plt.scatter(*zip(*f))

    def _gradient_color(self):
        """
        Private method colorizing our points in a gradient style.

        Variables:
        ----------
            r (ndarray): Identity-matrix.
            C (ndarray): Array for memorizing integers associated with values.
            X (ndarray): Array for points within our triangle.
        Returns:
        --------
            self.C and self.X now contains values.
        """
        r = np.identity(self.n)
        C = np.zeros(self.steps)
        X = np.zeros((self.steps, 2))

        for i in range(0, self.steps - 1):
            j = np.random.randint(self.n)
            C[0] = j
            corner = self._c_marked[j]
            C[i + 1] = (C[i] + j) / 2
            X[i + 1] = self.r * X[i] + (1 - self.r) * corner
        self.C = C[5:]
        self.X = X[5:]
        return self.C, self.X

    def plot(self, color=True, cmap="jet"):
        """
        Method for plotting with and without color given
        certain circumstances. Within this code is two exercises,
        one is commented out for better usage

        Variables:
        ----------
            color (boolean expression): False gives black color and true gives
            several colors.
            cmap (colormap): Certain set of colors.
        Returns:
        --------
            None, only plots.
        """
        if color == False:
            plt.scatter(*zip(*self.X_next), s=0.1, marker=".", color= "black")

        """
        #Exercise 2E
        if color == True:
            import random
            number_of_colors = self.n
            color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                         for i in range(number_of_colors)]
            #color_list = np.zeros((int(len(self.colors) / self.n), 2))

            for i in range(self.n):
                plt.scatter(*zip(*self.X_next[self.colors == i]), s=0.1, marker=".", color = f"{color[i]}" )
        """
        # Exercise 2F

        if color == True:
            C, X = self._gradient_color()
            plt.scatter(*zip(*X), c=C, s=1)

    def savepng(self, outfile, color=False, cmap="jet"):
        """
        Method for checking filetype and adding extension if necessary.

        Variables:
        ----------
            outfile (string): Name of our file we wish to save plot as.
            color (boolean expression): False, does not change our color in
            current circumstance.
            cmap (colormap): Certain set of colors.
        Returns:
        --------
            None, only plots saves figure.
        """
        picture = outfile
        if picture[-4:] == ".png":
            plt.savefig(f"figures/{outfile}", dpi=300, transparent=True)

        elif picture.find(".") == True:
            raise TypeError("File is already an extensions!")

        else:
            outline = outfile + ".png"
            plt.savefig(f"figures/{outfile}", dpi=300, transparent=True)


if __name__ == "__main__":

    plt.axis('equal')
    plt.axis('off')

    f = ChaosGame(n = 3, r = 1/2)
    f.plot_ngon()
    f._starting_point()
    f.iterate(steps = 20000, discard = 5)
    f.plot()
    f.savepng(outfile = "chaos1.png")
    plt.show()

    g = ChaosGame(n = 4, r = 1/3)
    g.plot_ngon()
    g._starting_point()
    g.iterate(steps = 20000, discard = 5)
    g.plot()
    g.savepng(outfile = "chaos2.png")
    plt.show()

    h = ChaosGame(n = 5, r = 1/3)
    h.plot_ngon()
    h._starting_point()
    h.iterate(steps = 20000, discard = 5)
    h.plot()
    h.savepng(outfile = "chaos3.png")
    plt.show()

    j = ChaosGame(n = 5, r = 3/8)
    j.plot_ngon()
    j._starting_point()
    j.iterate(steps = 20000, discard = 5)
    j.plot()
    j.savepng(outfile = "chaos4.png")
    plt.show()

    k = ChaosGame(n = 6, r = 1/3)
    k.plot_ngon()
    k._starting_point()
    k.iterate(steps = 20000, discard = 5)
    k.plot()
    k.savepng(outfile = "chaos5.png")

    """
    #Exercise 2B

    for i in range(3,9):
        A = ChaosGame(n = i, r = 1/2)
        A.plot_ngon()
        plt.show()
    """

    """
    #Exercise 2C

    iterations = 1000
    n = 5
    X = []
    for _ in range(iterations):
        f._starting_point()
        x = f.X
        X.append(x)
    plt.scatter(*zip(*X), s=0.3, marker=".", color="black")
    """

    """
    #Exercise 2E

    S = ChaosGame(n = 3, r = 1/2)
    S._starting_point()
    S.iterate(steps = 20000, discard = 5)
    S.plot(color=True, cmap="jet")
    plt.show()

    """
