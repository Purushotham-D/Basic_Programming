# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:54:36 2021

@author: PURUBOI
"""
def sqrt(n):
    
    return n**(1/2)

def perfectSquare(n):
    
    a=int(sqrt(n))
    
    if (a*a) == n:
        
        return True
    
    else:
        
        return False


n=int(input())
i,c=1,0
while c<n:
    
    if perfectSquare(i):
        print(i)
        c+=1
    i+=1