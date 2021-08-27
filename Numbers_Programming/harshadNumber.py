# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 11:54:13 2021

@author: PURUBOI
"""

def harshadNumber(n):
    temp=n
    s=0
    while n:
       rem=n%10
       n//=10
       s+=rem
    return temp%s==0
           
for i in range(1,100):
    if harshadNumber(i):
        print(i)



