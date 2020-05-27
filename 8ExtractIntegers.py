#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 23:09:14 2020

@author: liweichen
"""


def extract_increasing(digits):
    #l = len(digits)
    mylist = []
    dig = digits[0]
    firstnum = int(dig)
    mylist.append(firstnum)
    #print(mylist)
    dignew = digits.replace(dig,'',1)
    
    n = 1
    while dignew: 
        dignext = dignew[:n]
        nextnum = int(dignext)
       
        while nextnum<=firstnum:
             n = n+1
             dignext = dignew[:n]
             nextnum = int(dignext)
       
        mylist.append(nextnum)
        firstnum = nextnum
        dignew = dignew.replace(dignext,'',1)
        if dignew and dignew[0]=='0':
            dignew = dignew.replace('0','',1)
    
        l = len(dignew)
        if n>l:
            break
   
    return mylist
            
            
        
    
    