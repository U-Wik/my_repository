"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    The sum of two numbers

    Parameters
    ----------
    a : first number, integer or float
    b : first number, integer or float

    Returns
    -------
    float
        Description of an anonymous value

    Examples
    --------
    >>> simple_math.simple_add(1,3)
    4

    """
    return a+b

def simple_sub(a,b):
    """
    The diference between two numbers

    Parameters
    ----------
    a : first number, integer or float
    b : first number, integer or float

    Returns
    -------
    float
        Description of an anonymous value

    Examples
    --------
    >>> simple_math.simple_sub(1,3)
    -2

    """
    return a-b

def simple_mult(a,b):
    """
    The product of two numbers
    
    Parameters
    ----------
    a : first number, integer or float
    b : first number, integer or float

    Returns
    -------
    float
        Description of an anonymous value

    Examples
    --------
    >>> simple_math.simple_mult(1,3)
    3

    """
    return a*b

def simple_div(a,b):
    """
    The ratio between two numbers
    
    Parameters
    ----------
    a : first number, integer or float
    b : first number, integer or float, must not be zero

    Returns
    -------
    float
        Description of an anonymous value

    Warnings
    --------
    b must not be zero

    Examples
    --------
    >>> simple_math.simple_div(3,1)
    3

    """
    return a/b

def poly_first(x, a0, a1):
    """
    Calculates a first order polynom for a given x as a0 + a1*x
    
    Parameters
    ----------
    a : first number, integer or float
    b : first number, integer or float

    Returns
    -------
    float
        Description of an anonymous value

    Examples
    --------
    >>> simple_math.poly_first(1,3,2)
    5

    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    Calculates a second order polynom for a given x
    using poly_first as poly_first(x, a0, a1) + a2*(x**2)
    
    Parameters
    ----------
    a : first number, integer or float
    b : first number, integer or float

    Returns
    -------
    float
        Description of an anonymous value

    Examples
    --------
    >>> simple_math.poly_second(1,3,2,5)
    30

    """
    return poly_first(x, a0, a1) + a2*(x**2)

