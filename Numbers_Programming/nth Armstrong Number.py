# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 11:40:41 2021

@author: PURUBOI
"""

def armStrong(n):
    temp=n
    res=0
    while n:
        rem=n%10
        n//=10
        res+=rem**3
    return temp==res

n=int(input())
i,c=1,0
while c<n:
    
    if armStrong(i):
        print(i)
        c+=1
    i+=1