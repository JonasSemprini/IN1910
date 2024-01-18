from chaos_game import ChaosGame
import numpy as np
import matplotlib.pyplot as plt


def test_correct_r():
    """
    Tests the constructor of the class ChaosGame by assigning a
    forbidden and correct r value
    """
    correct = ChaosGame(3, 1 / 2)
    false = ChaosGame(3, 1.5)
    print("n and r values tested.", correct, false)

def test_correct_n():
    """
    Tests the constructor of the class ChaosGame by assigning a
    forbidden and correct n value
    """
    correct = ChaosGame(3, 1 / 2)
    false = ChaosGame(4.5, 1 / 2)
    print("n and r values tested.", correct, false)


def test_array_lengths_color_and_X():
    tol = 1e-7
    f = ChaosGame(3, 1 / 2)
    f._generate_ngon()
    f._starting_point()
    f.iterate(steps = 1000)
    f._gradient_color()
    success = abs(len(f.X) - len(f.C)) < tol
    msg = f"The two arrays are of different size!, C is {len(f.C)} and X is {len(f.X)}"
    assert success, msg

def test_random():
    # Test for random n and r values that our n-gon is reasonable.
    for i in range(4, 6):
        n = np.random.randint(3, 7)
        r = np.random.random()
        test = ChaosGame(n, r)
        test._starting_point()
        test.iterate(10000)
        test.plot_ngon()
        plt.show()
