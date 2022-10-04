from math_series.series import lucas

def test_zero():
    actual=lucas(0)
    excepted= 2
    assert actual == excepted
def test_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_str():
    actual=lucas("num")
    expected= "please enter only numbers!!"
    assert actual == expected

def test_three():
    actual=lucas(3)
    expected= 4
    assert actual == expected

def test_four():
    actual=lucas(4)
    expected= 7
    assert actual == expected

def test_seven():
    actual=lucas(7)
    expected= 29
    assert actual == expected

def test_eight():
    actual=lucas(8)
    expected= 47
    assert actual == expected

def test_negative_number():
    actual=lucas(-11)
    expected= "please enter positive numbers!!"
    assert actual == expected