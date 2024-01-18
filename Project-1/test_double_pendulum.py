import numpy as np
from double_pendulum import DoublePendulum


def test_equilibrium_double():
    tol = 1e-4
    M1 = 1
    L1 = 1
    M2 = 1
    L2 = 1
    f = DoublePendulum(M1, L1, M2, L2)
    computed = f.solve((0, 0, 0, 0), 10, 1000, "rad")
    expected = (0, 0, 0, 0)
    for i in range(0, len(computed)):
        success = (
            abs(expected[0] - computed[1][i]) < tol
            and abs(expected[1] - computed[2][i]) < tol
            and abs(expected[2] - computed[3][i]) < tol
            and abs(expected[3] - computed[4][i]) < tol
        )
        msg = "Fault in code"
        assert success, msg


def test_total_energy():
    """
    The chaotic system is unpredictable, hence
    a small, but not miniscule, change in total energy.
    We check to see if the change is constant
    """
    tol = 1
    M1 = 1
    L1 = 1
    M2 = 1
    L2 = 1
    f = DoublePendulum(L1, M1, L2, M2)
    f.solve(((2 * np.pi) / 3, 0, (2 * np.pi) / 5, 0), 20, 3000, "rad")
    computed = np.zeros(len(f.kinetic))
    for i in range(0, len(f.kinetic)):
        computed[i] = f.total_energy[i]
        expected = 36
        success = abs(computed[i] - expected) < tol
        msg = f"Fault in code, {computed} is not {expected} "
        assert success, msg


def test_double_pendulum_call():
    f = DoublePendulum(1, 1, 1, 1)
    Error = False
    try:
        f.kinetic, f.vx1, f.total_energy
    except ValueError:
        Error = True
    assert Error