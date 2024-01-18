import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation
from matplotlib.animation import *

g = 9.81


class DoublePendulum:
    """
    ==============================================
    Class DoublePendulum implemented to express,
    and solve the differential system shown in the __call__, method.
    ==============================================
    """

    def __init__(self, M1, L1, M2, L2):
        """
        Constructs all necessary attributes for the f object

        Arguments:
        ----------
            M1 (int/float): Weight of first pendulum
            L1 (int/float): Length of first pendulum
            M2 (int/float): Weight of second pendulum
            L2 (int/float): Length of second pendulum
            self.solution(Bool): Initial set to false, if not the solve method is called upon
        """
        self.M1 = M1
        self.M2 = M2
        self.L1 = L1
        self.L2 = L2
        self.solution = False

    def __call__(self, t, u):
        """
        Special method computing the differential equation
        Arguments:
        ----------
            t (scalar): intial time value
            u (ndarray): Differential values to compute the Jacobian

        Returns:
        --------
            [ndarray]: Solution values to the rhs of the ODE
        """
        M1 = self.M1
        M2 = self.M2
        L1 = self.L1
        L2 = self.L2
        delta_theta = u[2] - u[0]

        d_omega1 = (
            M2 * L1 * u[1] ** 2 * np.sin(delta_theta) * np.cos(delta_theta)
            + M2 * g * np.sin(u[2]) * np.cos(delta_theta)
            + M2 * L2 * u[3] ** 2 * np.sin(delta_theta)
            - (M1 + M2) * g * np.sin(u[0])
        ) / ((M1 + M2) * L1 - M2 * L1 * np.cos(delta_theta) ** 2)

        d_omega2 = (
            -M2 * L2 * u[3] ** 2 * np.sin(delta_theta) * np.cos(delta_theta)
            + (M1 + M2) * g * np.sin(u[0]) * np.cos(delta_theta)
            - (M1 + M2) * L1 * u[1] ** 2 * np.sin(delta_theta)
            - (M1 + M2) * g * np.sin(u[2])
        ) / ((M1 + M2) * L2 - M2 * L2 * np.cos(delta_theta) ** 2)

        d_theta1 = u[1]

        d_theta2 = u[3]

        return (d_theta1, d_omega1, d_theta2, d_omega2)

    def solve(self, y0, T, dt, msg_ang):
        """
        Instance method for solving the differential system.

        Arguments:
        ----------
            y0 (tuple, list): Intital conditions for theta1, omega1, theta2 and omega2
            T (int): End of time interval
            dt (int): Number of time points
            msg_ang (string): Message for converting angles into radians
            self.solution (bool): Set to True when the solve method is called
        """
        t_values = np.linspace(0, T, dt)
        if msg_ang == "rad":
            y0 = y0
        elif msg_ang == "Degrees":
            y0 = np.radians(y0)
        sol = solve_ivp(self, (0, T), y0, t_eval=t_values, method="Radau")
        self._t = sol.t
        self.solution = True
        self._theta1, self._omega1, self._theta2, self._omega2 = sol.y

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
            raise ValueError("Solve method has not been called.")
        else:
            return self._t

    @property
    def theta1(self):
        """

        Property for theta1 values

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon

        Returns:
        --------
            [ndarray]: Returns an n-dimensional array of theta1 values
        """
        if not self.solution:
            raise ValueError("Solve method has not been called.")
        else:
            return self._theta1

    @property
    def theta2(self):
        """

        Property for theta2 values

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon

        Returns:
        --------
            [ndarray]: Returns an n-dimensional array of theta2 values
        """
        if not self.solution:
            raise ValueError("Solve method has not been called.")
        else:
            return self._theta2

    @property
    def omega1(self):
        """

        Property for omega1 values

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon

        Returns:
        --------
            [ndarray]: Returns an n-dimensional array of omega1 values
        """
        if not self.solution:
            raise ValueError("Solve method has not been called.")
        else:
            return self._omega1

    @property
    def omega2(self):
        """

        Property for omega2 values

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon

        Returns:
        --------
            [ndarray]: Returns an n-dimensional array of omega2 values
        """
        if not self.solution:
            raise ValueError("Solve method has not been called.")
        else:
            return self._omega2

    @property
    def x1(self):
        """

        Property for converting from polar to cartesian coordinates (x-direction)

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon

        Returns:
        --------
            [ndarray]: Returns an n-dimensional array of x-values
        """
        if not self.solution:
            raise ValueError("Solve method has not been called.")
        else:
            return self.L1 * np.sin(self.theta1)

    @property
    def x2(self):
        """

        Property for converting from polar to cartesian coordinates,
        relative to pendulum one (x-direction)

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon

        Returns:
        --------
            [ndarray]: Returns an n-dimensional array of x2-values
        """
        if not self.solution:
            raise ValueError("Solve method has not been called.")
        else:
            return self.x1 + self.L2 * np.sin(self.theta2)

    @property
    def y1(self):
        """

        Property for converting from polar to cartesian coordinates (y-direction)

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon

        Returns:
        --------
            [ndarray]: Returns an n-dimensional array of y-values
        """
        if not self.solution:
            raise ValueError("Solve method has not been called.")
        else:
            return -self.L1 * np.cos(self.theta1)

    @property
    def y2(self):
        """

        Property for converting from polar to cartesian coordinates,
        relative to pendulum one (y-direction)

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon

        Returns:
        --------
            [ndarray]: Returns an n-dimensional array of y2-values
        """
        if not self.solution:
            raise ValueError("Solve method has not been called.")
        else:
            return self.y1 - self.L2 * np.cos(self.theta2)

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
            raise ValueError("Solve method has not been called.")
        else:
            P1 = self.M1 * g * (self.y1 + self.L1)
            P2 = self.M2 * g * (self.y2 + self.L1 + self.L2)
            return P1 + P2

    @property
    def vx1(self):
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
            raise ValueError("Solve method has not been called.")
        else:
            return np.gradient(self.x1, self.t)

    @property
    def vx2(self):
        """
        Property for computing velocity in the x2-direction

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon
        Returns:
        --------
        [ndarray]: Returns an n-dimensional array of v_x2 values
        """
        if not self.solution:
            raise ValueError("Solve method has not been called.")
        else:
            return np.gradient(self.x2, self.t)

    @property
    def vy1(self):
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
            raise ValueError("Solve method has not been called.")
        else:
            return np.gradient(self.y1, self.t)

    @property
    def vy2(self):
        """
        Property for computing velocity in the y2-direction

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon
        Returns:
        --------
        [ndarray]: Returns an n-dimensional array of v_y2 values
        """
        if not self.solution:
            raise ValueError("Solve method has not been called.")
        else:
            return np.gradient(self.y2, self.t)

    @property
    def kinetic(self):
        """
        Property for computing the kinetic energy of the double pendulum

        Raises:
        -------
            ValueError: Raises ValueError if the solve method,
            is not called upon
        Returns:
            [ndarray]: Returns an n-dimensional array of kinetic energy values
        """
        if not self.solution:
            raise ValueError("Solve method has not been called.")
        else:
            K1 = 0.5 * self.M1 * (self.vx1 ** 2 + self.vy1 ** 2)
            K2 = 0.5 * self.M2 * (self.vx2 ** 2 + self.vy2 ** 2)
            return K1 + K2

    @property
    def total_energy(self):
        """
        Property for computing the total energy of the double pendulum

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

    def create_animation(self):
        """

        ================================================================
        Instance method for creating an animation of the double pendulum
        ================================================================

        """
        fig = plt.figure()
        plt.axis("equal")
        # plt.axis('off')
        plt.axis([-3, 3, -3, 3])
        (self.pendulums,) = plt.plot([], [], "o--", lw=1)
        self.animation = FuncAnimation(
            fig,
            self._next_frame,
            frames=range(0, len(self.x1)),
            repeat=True,
            interval=15,
            blit=True,
        )

    def _next_frame(self, i):
        """
        Instance method to generate the next frame in the animation
        Arguments:
        ----------
            i (int): Frame number

        Returns:
        --------
            [ndarray]: Sequence of frames
        """
        self.pendulums.set_data(
            (0, self.x1[i], self.x2[i]), (0, self.y1[i], self.y2[i])
        )
        return (self.pendulums,)

    def save_animation(self, filename="example_simulation.mp4"):
        """
        Instance method for saving the animation

        Arguments:
        ----------
            filename (str) = Filename of the animation
        """
        self.animation.save(filename, fps=60)

    def show_animation(self):
        plt.show()


if __name__ == "__main__":
    M1 = 1
    L1 = 1
    M2 = 1
    L2 = 1
    f = DoublePendulum(M1, L1, M2, L2)
    # t, u0, u1, u2, u3 = f.solve(
    #     (-2 * np.pi / 3, 0, 4 * np.pi / 5, 0), 20, 600, msg_ang="rad"
    # )