#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 18:50:20 2020

@author: liweichen
"""


def double_trouble(items, n):
    n-=1
    if n<len(items):
        return items[n]
    else:
        pre=len(items)
        i=1
        while pre<n:
            i=i*2
            #print(pre)
            if pre+i*len(items)>n:
                break
            pre+=i*len(items)
            #print(pre)
        count = n-pre
        index = int(count/i)
        #print(n, i, pre, count, index)
    return items[index]
            
        