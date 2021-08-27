# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 15:00:58 2021

@author: PURUBOI
"""

def square(n):
    return n*n

def automorphic(n):
    
    a=square(n) 
    n1=len(str(n))  
    last = a%(10**n1)
    
    return n==last


for i in range(1000):
    
    if automorphic(i):
        print(i)
        
        
        
