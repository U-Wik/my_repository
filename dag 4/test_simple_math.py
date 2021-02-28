# test_simple_math
import simple_math

def test_simple_add():
    assert simple_math.simple_add(3,2)==5

def test_simple_sub():
    assert simple_math.simple_sub(3,2)==1

def test_simple_mult():
    assert simple_math.simple_mult(3,2)==6

def test_simple_div():
    assert simple_math.simple_div(3,2)== 1.5

def test_poly_first():
    assert simple_math.poly_first(5,3,2)==13

def test_poly_second():
    assert simple_math.poly_second(5,3,2,1)==38

    
