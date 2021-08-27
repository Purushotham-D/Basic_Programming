# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:42:39 2021

@author: PURUBOI
"""
import time as t

def factorial(n):
    fact=1
    while n>1:
        fact*=n
        n-=1
    return fact
t1=t.time()
print(factorial(115))
t2=t.time()
print(t2-t1)


# using recursion 

def factorialRecur(n,fact=1):
    
    if n==1:
        return fact
    fact*=n
    return factorialRecur(n-1,fact)

t3=t.time()
print(factorialRecur(115))
t4=t.time()
print(t4-t3)