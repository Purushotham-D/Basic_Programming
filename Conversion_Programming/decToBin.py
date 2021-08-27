# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 09:52:24 2021

@author: PURUBOI
"""

def decimalToBinary(n):
    res=''
    while n!=0:
        rem=n%2
        n=n//2
        res=str(rem)+res
    print('0b'+res)
    print(res)

n=int(input("Enter the positive number to convert from deci to bin: "))

decimalToBinary(n)

