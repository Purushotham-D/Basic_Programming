# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 09:52:24 2021

@author: PURUBOI
"""

def HexadecimalToDecimal(n):
    i=len(n)-1
    j,res=0,0
    while i>=0:
        if 'A'<=n[j]>='F':
            res+=(16**i)*(ord(n[j])-55)
        if 'a'<=n[j]>='f':
            res+=(16**i)*(ord(n[j])-87)
        else:
            res+=(16**i)*int(n[j])
        i-=1
        j+=1
    print(res)

n=input("Enter the positive number to convert from octal to decimal: ")
HexadecimalToDecimal(n)

