# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 11:54:13 2021

@author: PURUBOI
"""

def perfectNumber(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s==n
           
for i in range(1,100):
    if perfectNumber(i):
        print(i)

