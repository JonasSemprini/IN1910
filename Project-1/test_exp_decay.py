from exp_decay import ExponentialDecay


def test_exp_decay():
    f = ExponentialDecay(0.4)
    solve = f(0, 3.2)
    exp = -1.28
    tol = 1e-10
    assert abs(solve - exp) < tol
test_exp_decay()
