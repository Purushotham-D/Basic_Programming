# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:04:53 2021

@author: PURUBOI
"""

def sub(a,b):
    while (b!=0):
        borrow=(~a)&b
        a=a^b
        b=borrow<<1
    return a

def subrecur(a,b):
    if (b==0):
        return a
    else:
        return subrecur(a^b, ((~a)&b)<<1)


sub(27,22)
subrecur(35, 34)

