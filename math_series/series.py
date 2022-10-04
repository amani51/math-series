'''
This file has 3 functions:
1. fibonacci(n): that takes one parameter
    and returns the nth value in the fibonacci series.
2. lucas(n): that takes one parameter.
    and returns the nth value in the lucas series.
3. sum_series(n,num1,num2): that takes one parameter and two optional parameters(num1,num2);
    if user enter only one parameter the function will call fibonacci(n)
    else if user enter three parameter3 and num1=2&num2=1 the function will call lucas(n)
    else if user enter other values for the optional parameters it will produce other series.
'''

def fibonacci(n):
    if type(n)!= int:
        return "please enter only numbers!!"
    elif n<0:
        return "please enter positive numbers!!"   
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def lucas(n):
    if type(n)!= int:
        return "please enter only numbers!!"
    elif n<0:
        return "please enter positive numbers!!"   
    elif n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

def sum_series(n,num1=0,num2=1):
    if type(n)!= int or type(num1)!= int or type(num2)!= int:
        return "please enter only numbers!!"
    elif n<0:
        return "please enter positive numbers!!" 
    elif num1==0 and num2==1:
        return fibonacci(n)
    elif num1==2 and num2==1:
        return lucas(n)
    else:
        if n==0:
            return num1
        elif n==1:
            return num2
        else:
            return sum_series(n-1,num1,num2)+sum_series(n-2,num1,num2)

if __name__=="__main__":
    print("fibonacci(3) = ",fibonacci(3))
    print("fibonacci('num')",fibonacci("num"))
    print("lucas(7) = ",lucas(7))
    print("lucas(-11)",lucas(-11))
    print("sum_series(2) = ",sum_series(2))
    print("sum_series(4,2,1) = ",sum_series(4,2,1))
    print("sum_series(3,3,3) = ",sum_series(3,3,3))