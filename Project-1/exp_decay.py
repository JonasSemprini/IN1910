import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


class ExponentialDecay:
    """

    ==============================================
    Class ExponentialDecay implemented to express,
    and solve the differential system du/dt = -a*u
    ==============================================

    """

    def __init__(self, a):
        """
        Constructs all necessary attributes for the f object

        Arguments:
        ---------
            a (float): Decay constant
        """
        self.a = a

    def __call__(self, t, u):
        """
        Special method computing the differential equation
        Arguments:
        ---------
            t (scalar): Starting time point for the differtial system
            u (ndarray): Solution values to the differential system based on inital conditions

        Returns:
        --------
            array : Solution values to the ODE
        """
        dudt = -self.a * u
        return dudt

    def solve(self, T, u0, dt):
        """
        Instace method for solving the ODE

        Arguments:
        ----------
            T (tuple/list): Time interval
            u0 (tuple/list): Inital conditions
            dt (ndarry): Time intervall with time steps

        Returns:
            [ndarray]: Solutions to the ODE
        """
        sol = solve_ivp(self.__call__, T, u0, t_eval=dt)
        return sol.t, sol.y[0]


if __name__ == "__main__":
    f = ExponentialDecay(0.4)
    t, u = f.solve((1, 5), (2,), np.linspace(1, 5, 20))
    plt.plot(t, u)
    plt.show()
