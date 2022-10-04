from math_series.series import sum_series

def test_zero():
    actual=sum_series(0)
    excepted=0
    assert actual == excepted

def test_zero_with_options():
    actual=sum_series(0,2,1)
    excepted=2
    assert actual == excepted

def test_one():
    actual=sum_series(1)
    excepted=1
    assert actual == excepted

def test_one_with_options():
    actual=sum_series(1,2,1)
    excepted=1
    assert actual == excepted

def test_str():
    actual=sum_series("str","str2","str3")
    excepted="please enter only numbers!!"
    assert actual == excepted

def test_two():
    actual=sum_series(2)
    excepted=1
    assert actual == excepted

def test_two_with_options():
    actual=sum_series(2,2,1)
    excepted=3
    assert actual == excepted

def test_zero_other_option1():
    actual=sum_series(0,0,2)
    excepted=0
    assert actual == excepted

def test_zero_other_option2():
    actual=sum_series(0,2,1)
    excepted=2
    assert actual == excepted

def test_three_other_option1():
    actual=sum_series(3,3,3)
    excepted=9
    assert actual == excepted

def test_three_other_option2():
    actual=sum_series(3,0,3)
    excepted=6
    assert actual == excepted

def test_ten_other_option1():
    actual=sum_series(10,1,0)
    excepted=34
    assert actual == excepted

def test_negative_number():
    actual=sum_series(-11,2,5)
    expected= "please enter positive numbers!!"
    assert actual == expected