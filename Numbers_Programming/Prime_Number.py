# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 17:33:29 2021

@author: PURUBOI
"""

def prime(n):
    
        if n>1:
            for i in range(2,n//2+1):
                if n%i==0:
                    return False
            else:
                return True
        else:
            return False
        
m,n=int(input("enter no 1 : ")),int(input("enter no 2 : "))        
for i in range(m,n):
        if (prime(i)):
            print(i)

