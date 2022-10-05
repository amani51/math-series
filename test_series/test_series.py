from math_series.series import sum_series ,fibonacci,lucas
import pytest
######################### test_fibonacci #############################
def test_zero_fibonacci():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_one_fibonacci():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_str_fibonacci():
    actual=fibonacci("num")
    expected= "please enter only numbers!!"
    assert actual == expected

def test_four_fibonacci():
    actual=fibonacci(4)
    expected= 3
    assert actual == expected

def test_seven_fibonacci():
    actual=fibonacci(7)
    expected= 13
    assert actual == expected

def test_negative_number_fibonacci():
    actual=fibonacci(-11)
    expected= "please enter positive numbers!!"
    assert actual == expected

######################### test_lucas #############################
def test_zero_lucas():
    actual=lucas(0)
    excepted= 2
    assert actual == excepted
def test_one_lucas():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_str_lucas():
    actual=lucas("num")
    expected= "please enter only numbers!!"
    assert actual == expected

def test_four_lucas():
    actual=lucas(4)
    expected= 7
    assert actual == expected

def test_eight_lucas():
    actual=lucas(8)
    expected= 47
    assert actual == expected

def test_negative_number_lucas():
    actual=lucas(-11)
    expected= "please enter positive numbers!!"
    assert actual == expected

######################### test_sum_series #############################
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