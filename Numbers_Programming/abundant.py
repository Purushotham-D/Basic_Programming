# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 13:09:05 2021

@author: PURUBOI
"""

def abundant(n):
    
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s>n

for i in range(100):
    if abundant(i):
        print(i)

