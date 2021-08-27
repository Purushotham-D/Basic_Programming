# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 18:42:13 2021

@author: PURUBOI
"""

def digitPalindrome(n):
  s=str(n)
  c=s[-1::-1]
  if s[0]==c[0]:
    return True
def getter():
    l=[None]*N
    for i in range(len(l)):
        l[i]=list(map(int,input().split(" ")))
    return l

N=int(input())
l=getter()
    
for j in range(len(l)):
  res=0
  a,b=l[j][0],l[j][1]
  for i in range(a,b):
    if digitPalindrome(i):
      res=res+1
  print(res)
  
  