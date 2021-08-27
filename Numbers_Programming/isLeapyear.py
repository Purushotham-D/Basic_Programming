# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 15:49:02 2021

@author: PURUBOI
"""

year= int(input("enter the year to check Leap year or Not: "))

def isLeap(year):
    
    if year%4==0 and year%100!=0 or year%400==0:
        print("Leap Year")
    else:
        print("Not a Leap Year")
        
isLeap(year)




