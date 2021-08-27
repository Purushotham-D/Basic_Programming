# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 16:17:14 2021

@author: PURUBOI
"""
import time 

def prime_Factors(n):
    
    def prime(n):
    
        if n>1:
            for i in range(2,(n//2)+1):
                if n%i==0:
                    return False
            else:
                return True
        else:
            return False
            
    s=list()
    
    for i in range(1,(n//2)+1):
        if n%i==0:
            s.append(i)
            
    for i in s:
        if (prime(i)):
            print(i)
    
t1=time.time()
prime_Factors(34)
t2=time.time()
print(t2-t1)
