# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 09:52:24 2021

@author: PURUBOI
"""

def decimalToOct(n):
    res=''
    while n!=0:
        rem=n%8
        n=n//8
        res=str(rem)+res
    print('0o'+res)

n=int(input("Enter the positive number to convert from deci to octal : "))

decimalToOct(n)

