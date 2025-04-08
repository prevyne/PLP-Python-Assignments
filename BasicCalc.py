#!/usr/bin/env/ python

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
operator=str(input("Enter the operator (+, -, *, /): "))
result=0

if operator=='+':
    result=num1+num2
elif operator=='-':
    result=num-num2
elif operator=='*':
    result=num1*num2
elif operator=='/':
    result=num1/num2

print("{} {} {} = {}".format(num1,operator,num2,result))
