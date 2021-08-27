# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 09:42:29 2021

@author: PURUBOI
"""
n=15
k=65+n-1
for i in range(n):
    for j in range(n):
        if (j+i>=n-1):
            print(chr(k),end=" ")
        else:
            print(" ",end=" ")
    k-=1
    print()