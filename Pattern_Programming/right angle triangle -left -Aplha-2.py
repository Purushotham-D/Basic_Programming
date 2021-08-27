# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 09:42:29 2021

@author: PURUBOI
"""
n=15
k=65
for i in range(n):
    for j in range(n):
        if (i==n-1 or j==0 or i==j or i>=j):
            print(chr(k),end=" ")
            k+=1
        else:
            print(" ",end=" ")
    k=65
    print()