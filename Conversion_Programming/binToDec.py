# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 09:52:24 2021

@author: PURUBOI
"""

def binaryToDecimal(n):
    i=len(n)-1
    j,res=0,0
    while i>=0:
        res+=((2**i)*int(n[j]))
        i-=1
        j+=1
    print(res)

n=input("Enter the positive number to convert from bin to decimal: ")
binaryToDecimal(n)

