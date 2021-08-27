# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:54:36 2021

@author: PURUBOI
"""
n=46
def sqrt(n):
    
    return n**(1/2)

def perfectSquare(n):
    
    a=int(sqrt(n))
    
    if (a*a) == n:
        
        return True
    
    else:
        
        return False

perfectSquare(46)    



