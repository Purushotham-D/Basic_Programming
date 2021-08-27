# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 09:52:24 2021

@author: PURUBOI
"""

def binToHexa(n):
    def binToDec(n):
        i=len(n)-1
        j=0
        res=0
        while i>=0:
            res+=((2**i)*int(n[j]))
            i-=1
            j+=1
        return int(res)
    
    def decimalToHexa(n):
        res=''
        while n!=0:
            rem=n%16
            n=n//16
            if 10<=rem<=15:
                res=chr(55+rem)+res
            else:
                res=str(rem)+res
                
        print('0x'+res)
        
    m=binToDec(n)
    decimalToHexa(m)

n=input("Enter the positive number to convert from deci to hexadecimal : ")
binToHexa(n)

