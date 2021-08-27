# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 15:59:31 2021

@author: PURUBOI
"""

def add(a,b):
    while (b!=0):
        carry=a&b
        a=a^b
        b=carry<<1
    return a

def addrecur(a,b):
    if (b==0):
        return a
    else:
        return addrecur(a^b, (a&b)<<1)


add(27,22)
addrecur(34, 35)
        