#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:24:50 2020

@author: liweichen
"""


def can_balance(items):
    if len(items) == 1:
        return 0
    elif len(items) == 2:
        return -1
    else:
        for i in range(1,len(items)-1):
            x=i-1
            y=i+1
            left, right = 0,0
            while x>=0:
                #print(x, items[x], i-x)
                left += items[x]*(i-x)
                x-=1
            while y<len(items):
                right += items[y]*(y-i)
                y+=1
            print(left, right)
            if left == right:
                return i
        return -1