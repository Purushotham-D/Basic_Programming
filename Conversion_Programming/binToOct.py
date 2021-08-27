# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 09:52:24 2021

@author: PURUBOI
"""

def binaryToOct(n):
    
    def binaryToDecimal(n):
        i=len(n)-1
        j,res=0,0
        while i>=0:
            res+=((2**i)*int(n[j]))
            i-=1
            j+=1
        return int(res)
     
    def decimaltoOct(n):
        res=''
        while n!=0:
            rem=n%8
            n=n//8
            res=str(rem)+res
        print('0o'+res)
        
    m=binaryToDecimal(n)
    decimaltoOct(m)
    

n=input("Enter the positive number to convert from bin to octal : ")
binaryToOct(n)

