import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

g = 9.81


class Pendulum:
    """
    ==============================================
    Class Pendulum implemented to express,
    and solve the differential system:
        dtheta/dt = omega
        domega/dt = -g/L * sin(theta)
    ==============================================
    """

    def __init__(self, L, M=1):
        """
        Constructs all necessary attributes for the f object

        Arguments:
        ----------
            L (int, float): Length of pendulum
            M (int, float): Mass of pendulum
            self.solution(Bool): Intial set to False if not the solve method is called
        """
        self.L = L
        self.M = M
        self.solution = False

    def __call__(self, t, u):
        """
        Special method computing the differential equation
        Arguments:
        ----------
        t (scalar): Starting time point for the differtial system
        u (ndarray): Differential values to compute the Jacobian
        Returns:
        --------
            [ndarray]: Solution values to the ODE
        """
        dthetadt = u[1]
        domegadt = -(g / (self.L)) * np.sin(u[0])
        u = (dthetadt, domegadt)
        return u

    def solve(self, y0, T, dt, msg_ang):
        """
        Instace method for solving the ODE
        ----------------------------------

        Arguments:
        ----------
            y0 (tuple/list): Inital conditions for theta and omega
            T (int/float): End of time interval
            dt (int): Number of timepoints in an ndarray
            msg_ang (string): Message for converting angles in radians
            self.solution(bool): Set to True, when solve is called
        """

        time_values = np.linspace(0, T, dt)
        if msg_ang == "rad":
            y0 = y0
        elif msg_ang == "deg":
            y0 = np.radians(y0)
        sol = solve_ivp(self, (0, T), y0, t_eval=time_values)
        self._t = sol.t
        self._theta, self._omega = sol.y
        self.solution = True

    @property
    def t(self):
        """

        Property for t-values in the ODE-solution

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon

        Returns:
        --------
            [ndarray]: Returns an n-dimensional array of time points
        """

        if not self.solution:
            raise ValueError("The solve method was not called")
        else:
            return self._t

    @property
    def theta(self):
        """
        Property for theta-values in the ODE-solution

        Raises:
        -------

            ValueError: Raises ValueError if the solve method,
            is not called upon

        Returns:
        --------
            [ndarray]: Returns an n-dimensional array of theta-values
        """
        if not self.solution:
            raise ValueError("The solve method was not called")
        else:
            return self._theta

    @property
    def omega(self):
        """
        Property for omega-values in the ODE-solution

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon
        Returns:
        --------
            [ndarray]: Returns an n-dimensional array of omega-values
        """
        if not self.solution:
            raise ValueError("The solve method was not called")
        else:
            return self._omega

    @property
    def x(self):
        """
        Property for converting polar coordinates to cartesian (x-values)

        Raises:
            ValueError: Raises ValueError if the solve method,
            is not called upon
        Returns:
            [ndarray]: Returns an n-dimensional array of x-values
        """
        if not self.solution:
            raise ValueError("The solve method was not called")
        else:
            return self.L * np.sin(self.theta)

    @property
    def y(self):
        """
        Property for converting polar coordinates to cartesian (y-values)

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon

        Returns:
        --------
            [ndarray]: Returns an n-dimensional array of y-values
        """
        if not self.solution:
            raise ValueError("The solve method was not called")
        else:
            return -self.L * np.cos(self.theta)

    @property
    def vx(self):
        """
        Property for computing velocity in the x-direction

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon
        Returns:
        --------
        [ndarray]: Returns an n-dimensional array of v_x values
        """
        if not self.solution:
            raise ValueError("The solve method was not called")
        else:
            return np.gradient(self.x, self.t)

    @property
    def vy(self):
        """
        Property for computing velocity in the y-direction
        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon
        Returns:
        --------
            [ndarray]: Returns an n-dimensional array of v_y values
        """
        if not self.solution:
            raise ValueError("The solve method was not called")
        else:
            return np.gradient(self.y, self.t)

    @property
    def potential(self):
        """
        Property for computing the potential energy of the single pendulum

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon
        Returns:
        --------
            [ndarray]: Returns an n-dimensional array of potential energy values
        """
        if not self.solution:
            raise ValueError("The solve method was not called")
        else:
            return self.M * g * (self.y + self.L)

    @property
    def kinetic(self):
        """
        Property for computing the kinetic energy of the single pendulum

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon
        Returns:
            [ndarray]: Returns an n-dimensional array of kinetic energy values
        """
        if not self.solution:
            raise ValueError("The solve method was not called")
        else:
            return self.M * (self.vx ** 2 + self.vy ** 2)

    @property
    def total_energy(self):
        """
        Property for computing the total energy of the single pendulum

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon
        Returns:
            [ndarray]: Returns an n-dimensional array of total energy values
        """
        if not self.solution:
            raise ValueError("Solve method has not been called.")
        else:
            t_energy = self.kinetic + self.potential
            return t_energy


class Dampened_Pendulum(Pendulum):
    """
    ==============================================
    Class Dampened_Pendulum implemented to express,
    and solve the differential system:
        dtheta/dt = omega
        domega/dt = (-g/l)sin(theta) - B/M(omega)
    via inheretance of Class Pendulum
    ==============================================
    Arguments:
    ----------
        Pendulum (class): Inheritance of all attributes, methods and properties in Pendulum.
    """

    def __init__(self, L, M=1, B=2):
        """
        Constructs all necessary attributes for the f object
        Arguments:
        ----------
            L (int, float): Length of Pendulum
            M (int, float: Mass of pendulum
            B (int, float): Dampening factor
        """
        Pendulum.__init__(self, L, M)
        self.B = B

    def __call__(self, t, u):
        """
        Special method computing the differential equation
        Arguments:
        ----------
            t (scalar): initial time point
            u (ndarray): Differential values to compute the Jacobian

        Returns:
            [ndarray]: Solution values to the ODE
        """
        dthetadt = u[1]
        domegadt = -(g / self.L) * np.sin(u[0]) - (self.B / self.M) * u[1]
        return (dthetadt, domegadt)


if __name__ == "__main__":
    L = 2.7
    f = Dampened_Pendulum(L)

    t, u0, u1 = f.solve((30, 3), 10, 100, msg_ang="deg")
    # plt.plot(t, f.kinetic, "k", label="Kinetic Energy")
    # plt.plot(t, f.potential, label="Potential Energy")
    plt.xlim([0, 10])
    plt.plot(t, f.total_energy, "b-", label="Total Energy")
    plt.legend()
    plt.show()
