# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 18:52:27 2021

@author: PURUBOI
"""

def sumofDigits(n):
    s=0
    while n:
        rem=n%10
        s=s+rem
        n//=10
    return s

def generic_root(n):
    
    while True:
        
        if n<=9:
            return n
        n=sumofDigits(n)

print(generic_root(45445))
print(generic_root(45))


