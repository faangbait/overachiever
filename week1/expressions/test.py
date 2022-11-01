from expressions import *
import sys
if 'pytest' not in sys.modules:
    print("Requires pytest -- pytest test.py")

def test_calc_math_expression():
    assert calc_math_expression(10,2,':') == 5.0
    assert calc_math_expression(10,-2,':') == -5.0
    assert calc_math_expression(10,2,'+') == 12.0
    assert calc_math_expression(10,2,'-') == 8.0
    assert calc_math_expression(10,2,'*') == 20.0
    
    
def test_calc_math_expression_from_str():
    assert calc_math_expression_from_str("10 : 2") == 5.0
    assert calc_math_expression_from_str("10 : -2") == -5.0
    assert calc_math_expression_from_str("-10 : -2") == 5.0
    assert calc_math_expression_from_str("-10 : 2") == -5.0
    assert calc_math_expression_from_str("10 + 2") == 12.0
    assert calc_math_expression_from_str("100 - 39.3") == 60.7
    assert calc_math_expression_from_str("5 : 2") == 2.5
    assert calc_math_expression_from_str("5 : 0") is None
    assert calc_math_expression_from_str("10 333 2") is None
    assert calc_math_expression_from_str("10 ^ 2") is None

def test_find_largest_and_smallest_numbers():
    assert find_largest_and_smallest_numbers(5, 1, 10) == (10, 1)
    assert find_largest_and_smallest_numbers(2.5, 2.5, 7) == (7, 2.5)
    assert find_largest_and_smallest_numbers(7, 2.5, 2.5) == (7, 2.5)
    assert find_largest_and_smallest_numbers(-5, -5, -5) == (-5, -5)
    assert find_largest_and_smallest_numbers(10, -1, 10) == (10, -1)
    assert find_largest_and_smallest_numbers(-2, 5, -2) == (5, -2)
    assert find_largest_and_smallest_numbers(3, 20, -2) == (20, -2)
    assert find_largest_and_smallest_numbers(7, 10, 0) == (10, 0)
    assert find_largest_and_smallest_numbers(10, 7, 0) == (10, 0)
    assert find_largest_and_smallest_numbers(0, 10.01, 10) == (10.01, 0)

def test_quadratic_equation_solver():
    assert quadratic_equation_solver(1, 1.5, -1) == (0.5, -2)
    assert quadratic_equation_solver(1, -8, 16) == (4, None)
    assert quadratic_equation_solver(1, -2, 34.5) == (None, None)
    assert quadratic_equation_solver(4, -12, 9) == (3/2, None)

def test_quadratic_equation_solver_from_string():
    assert quadratic_equation_solver_from_string("1 1.5 -1") == (0.5, -2)
    assert quadratic_equation_solver_from_string("1 -8 16") == (4, None)
    assert quadratic_equation_solver_from_string("1 -2 34.5") == (None, None)
    assert quadratic_equation_solver_from_string("4 -12 9") == (3/2, None)
    assert quadratic_equation_solver_from_string("4 two 0") == (None, None)
    
    
def test_temp_checker():
    assert temp_checker(26, 38, 90, 20) is True
    assert temp_checker(10, 10, 10, 10) is False
    assert temp_checker(10, 11, 10, 11) is True
    assert temp_checker(-1, -9, 0, 1) is True
    assert temp_checker(0, 90, 0, 1) is True
