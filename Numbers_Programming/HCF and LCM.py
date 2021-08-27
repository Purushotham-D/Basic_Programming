# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 14:59:02 2021

@author: PURUBOI
"""

# Find Factors of the given number 

def hcf(a,b):
    if a==0:
        return b
    return hcf(b%a,a)


def lcm(n1,n2):
    return (n1*n2)/hcf(n1,n2)


hcf(196,38024)

lcm(18,27)

lcm(196,38024)

 