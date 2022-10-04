from math_series.series import fibonacci


def test_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_str():
    actual=fibonacci("num")
    expected= "please enter only numbers!!"
    assert actual == expected

def test_three():
    actual=fibonacci(3)
    expected= 2
    assert actual == expected

def test_four():
    actual=fibonacci(4)
    expected= 3
    assert actual == expected

def test_seven():
    actual=fibonacci(7)
    expected= 13
    assert actual == expected

def test_eight():
    actual=fibonacci(8)
    expected= 21
    assert actual == expected

def test_negative_number():
    actual=fibonacci(-11)
    expected= "please enter positive numbers!!"
    assert actual == expected