# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 14:31:11 2021

@author: PURUBOI
"""

def ami(n):
    
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s/n

def amicable(n1,n2):
    a=ami(n1)
    b=ami(n2)
    if a==b:
        return True
    else:
        return False
    
amicable(6,12)
amicable(6,28)
amicable(28,50)