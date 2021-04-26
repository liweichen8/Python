#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 19:43:40 2020

@author: liweichen
"""


#import math

def counting_series(n):
    n+=1
    if n <= 9 :
        return n
    pre = 0
    i = 0
    while pre < n:
        i+=1
        if pre + i*9*10**(i-1) >= n:
            #i-=1
            #print(i, pre)
            break
        pre += i * 9 * 10**(i-1) #compare with n
    prenum = 10**(i-1)-1
    #count = math.ceil((n-pre)/i)
    if ((n-pre)/i)%1!=0:
        count = (n-pre)//i + 1
    else:
        count = (n-pre)//i
    print(n, pre, i, prenum)
    num = str(prenum+count)
    index = (n-pre)%i-1
    #print(n, pre, i)
    print(num, index, count)
    return num[index]
        
    
        