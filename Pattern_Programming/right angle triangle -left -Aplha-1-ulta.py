# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:33:39 2021

@author: PURUBOI
"""

n=15
k=65
for i in range(n):
    for j in range(n):
        if (i+j<=n-1):
            print(chr(k),end=" ")
        else:
            print(" ",end=" ")
    k+=1
    print()
    