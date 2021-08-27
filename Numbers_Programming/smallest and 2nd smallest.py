# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 15:31:52 2021

@author: PURUBOI
"""

a=[2,5,7,9,1,2,0]

b1=a[0]
b2=a[1]

for i in range(len(a)):
    if a[i]<b1:
        b2=b1
        b1=a[i]
print(b1,b2)