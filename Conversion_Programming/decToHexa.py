# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 09:52:24 2021

@author: PURUBOI
"""

def decimalToHexa(n):
    res=''
    while n!=0:
        rem=n%16
        n=n//16
        if 10<=rem<=15:
            res=chr(55+rem)+res
            #res=chr(87+rem)+res
        else:
            res=str(rem)+res
            
    print('0x'+res)

n=int(input("Enter the positive number to convert from deci to hexadecimal : "))

decimalToHexa(n)

