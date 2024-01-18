import calculator
from math import factorial
import numpy as np
import pytest

def test_add_exercise1():
    '''
    Test function checking the given input of add(x,y) against the corresponding output
    '''
    assert calculator.add(1,2) == 3
    #assert 1 == 3

test_add_exercise1()

def test_add_exercise2():
    '''
    Test function checking the given input of add(x,y) against the corresponding output,
    whereas the difference between output and the actual value is disciplined by a certain tolerance due to round-off errors.
    '''
    value1 = calculator.add(0.1, 0.2)
    value2 = 0.3
    tol = 1e-7
    result = abs(value1 - value2) < tol
    assert result

test_add_exercise2()

def test_add_exercise3():
    '''
    Test function checking the given input of add(x,y) against the corresponding output
    '''
    ord = calculator.add('Hello ', 'World')
    assert ord == 'Hello World'

test_add_exercise3()

def test_add_exercise4_factorial():
    '''
    Test function checking the given input of factorial1(n) against the math module factorial
    '''
    assert calculator.factorial1(340) == factorial(340)

test_add_exercise4_factorial()

def test_add_exercise4_sin():
    '''
    Test function checking the given input of sinus(x, n) against the corresponding output,
    whereas the difference between output and the actual value is disciplined by a certain tolerance due to round-off errors.
    '''
    approx = calculator.sinus(0.5, 10)
    correct = np.sin(0.5)
    tol = 1e-7
    result = abs(approx - correct) < tol
    assert result

test_add_exercise4_sin()

def test_add_exercise4_divide():
    '''
    Test function checking the given input of divide(x,y) against the corresponding output
    '''
    verdi1 = calculator.divide(1,2)
    verdi2 = 0.5
    tol = 1e-7
    resultat = abs(verdi1 - verdi2) < tol
    assert resultat
test_add_exercise4_divide()

def test_add_exercise4_exp():
    '''
    Test function checking the given input of exp(x, n) against the corresponding output,
    whereas the difference between output and the actual value is disciplined by a certain tolerance due to round-off errors.
    '''
    approx = calculator.exp(13, 50)
    correct = np.exp(13)
    tol = 1e-7
    resultat = abs(approx - correct) < tol
    assert resultat
test_add_exercise4_exp()

def test_add_exercise_4_multi():
    '''
    Test function checking the given input of multi(x,y) against the corresponding output
    '''
    assert calculator.multi(3,4) == 12
test_add_exercise_4_multi()

def test_add_exercise5_Type_Error():
    '''
    Pytest exception function, searching for TypeErrors
    '''
    with pytest.raises(TypeError):
        calculator.add(2, 'Nå er vi ute og kjøre')
test_add_exercise5_Type_Error()

def test_add_exercise5_Zero_Division():
    '''
    Pytest exception function, searching for ZeroDivisionErrors
    '''
    with pytest.raises(ZeroDivisionError):
        calculator.divide(2, 0)
test_add_exercise5_Zero_Division()

@pytest.mark.parametrize(
    "arg, expected_output", [[(2, -1), 1], [(0, 1), 1], [(1, 0), 1]]
)

def test_add_exercise6(arg, expected_output):
    assert calculator.add(arg[0], arg[1]) == expected_output


@pytest.mark.parametrize("arg2, expected_output2", [[(0.2, 0.3), 0.5], [(0.1, 0.9), 1]]
)
def test_add_excercise6_float(arg2, expected_output2):
    assert calculator.add(arg2[0], arg2[1]) == expected_output2

@pytest.mark.parametrize("arg3, expected_output3", [[('Hello ', 'World'), 'Hello World'], [('So long ', 'and thanks for all the fish'), 'So long and thanks for all the fish'],
[('Dette skal ', 'Gi feil'), 'Dette skal Gi feil']]
)

def test_add_excercise6_string(arg3, expected_output3):
    assert calculator.add(arg3[0], arg3[1]) == expected_output3

@pytest.mark.parametrize("arg4, expected_output4", [[5, 120], [4, 24], [3, 6]])

def test_add_exercise6_factorial(arg4, expected_output4):
    assert calculator.factorial1(arg4) == expected_output4

@pytest.mark.parametrize("arg5, expected_output5", [[(np.pi, 50), 0], [(np.pi/2, 50), 1], [(0, 50), 0]])

def test_add_exercise6_sin(arg5, expected_output5):
    value1 = calculator.sinus(arg5[0], arg5[1])
    value2 = expected_output5
    tol = 1e-7
    assert abs(value1 - value2) < tol

@pytest.mark.parametrize("arg6, expected_output6", [[(2, 2), 1], [(2, 5), 0.4], [(1, 2), 0.5]])

def test_add_exercise6_divide(arg6, expected_output6):
    value1 = calculator.divide(arg6[0], arg6[1])
    correct = expected_output6
    tol = 1e-7
    result = abs(correct - value1) < tol
    assert result

@pytest.mark.parametrize("arg7, expected_output7", [[(0, 20), 1], [(3, 20), np.exp(3)], [(5, 30), np.exp(5)]])

def test_add_exercise6_exp(arg7, expected_output7):
    value = calculator.exp(arg7[0], arg7[1])
    correct = expected_output7
    tol = 1e-6
    result = abs(correct - value) < tol
    assert result

@pytest.mark.parametrize("arg8, expected_output8", [[(5,6), 30], [(8, 2), 16], [(3, 6), 18]])

def test_add_exercise6_multi(arg8, expected_output8):
    assert calculator.multi(arg8[0], arg8[1]) == expected_output8
