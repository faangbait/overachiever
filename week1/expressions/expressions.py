import re, math

def calc_math_expression(num1, num2, operator):
    """
        Calculates a simple arithmetic expression

        Args:
            num1 (int)
            num2 (int)
            operator (str)
                One of +, -, *, or :
        """
    try:
        # Try typecast, return None if invalid
        num1 = float(num1)
        num2 = float(num2)
    except TypeError:
        return None

    try:
        match operator:
            case '+':
                return num1 + num2
            case '-':
                return num1 - num2
            case '*':
                return num1 * num2
            case ':':
                return num1 / num2
            case _:
                return None
    except ZeroDivisionError:
        return None

def calc_math_expression_from_str(str_input):
    """Parses a string to calculate an arithmetic expression"""
    matches = re.match(r'(?P<num1>(\d|-|\.)+) (?P<operator>.) (?P<num2>.*)', str_input)
    if matches is not None:
        num1 = matches.groupdict().get("num1", None)
        operator = matches.groupdict().get("operator", None)
        num2 = matches.groupdict().get("num2", None)
        return calc_math_expression(num1, num2, operator)
        

def find_largest_and_smallest_numbers(*args):
    """Returns a tuple of (largest, smallest)"""
    return (max(args), min(args))

def quadratic_equation_solver(a, b, c):
    """
        Solves a quadratic equation given a,b,c. Handles invalid input.

        Args:
            a (any)
            b (any)
            c (any)
        Returns: (float|None, float|None)
    """
    
    try:
        # Try typecast, return (None, None) if invalid
        a = float(a)
        b = float(b)
        c = float(c)
    except TypeError:
        return (None, None)

    # Handle 'not a quadratic'
    if a == 0:
        return (None, None)

    try:
        pos = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    except ValueError:
        pos = None
    
    try:
        neg = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    except ValueError:
        neg = None
    
    if pos == neg:
        # Has a single solution
        return (pos, None)
    return (pos, neg)

def quadratic_equation_solver_from_string(str_input):
    """Solves a quadratic equation given a string of three numbers"""
    matches = re.match(r'(?P<a>(\d|-|\.)+) (?P<b>(\d|-|\.)+) (?P<c>(\d|-|\.)+)', str_input)
    if matches is not None:
        return quadratic_equation_solver(
            matches.groupdict().get("a", None),
            matches.groupdict().get("b", None),
            matches.groupdict().get("c", None)
            )
    return (None, None)

def quadratic_equation_solver_from_user_input():
    str_input = input()
    return quadratic_equation_solver_from_string(str_input)

def temp_checker(min_temp, *args):
    """Returns true if two or more numbers are greater than min_temp"""
    count = 0
    for temp in args:
        if temp > min_temp:
            count += 1

    return count >= 2
