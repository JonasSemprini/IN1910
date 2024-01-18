from pendulum import Pendulum
import numpy as np


def test_pendulum_derivatives():
    tol = 1e-2
    f = Pendulum(2.7)
    computed = f.__call__(100, (np.pi / 6, 0.15))
    print(computed)
    expected = [0.15, -1.81]

    success = (
        abs(expected[0] - computed[0]) < tol and abs(expected[1] - computed[1]) < tol
    )
    msg = "Fault in code"
    assert success, msg


def test_pendulum_call():
    f = Pendulum(2.7)
    Error = False
    try:
        f.t, f.omega, f.theta
    except ValueError:
        Error = True
    assert Error


def test_pendulum_zero():
    f = Pendulum(1)
    g = f.solve((0, 0), 10, 10, "deg")
    for i in range(0, 100):
        if g[1][i] == 0 and g[2][i] == 0:
            return True
        else:
            assert False


def test_radius():
    tol = 1e-2
    L = 1
    f = Pendulum(L)
    f.solve((30, 0), 10, 1000, "deg")
    expected = L ** 2
    for i in range(0, len(f.x)):
        x = f.x[i]
        y = f.y[i]
        computed = x ** 2 + y ** 2
        success = abs(computed - expected) < tol
        msg = f"Fault in code, {computed} is not {expected} "
        assert success, msg
