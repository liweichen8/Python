#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:14:45 2020

@author: liweichen
"""


def nearest_smaller(items):
    num = []
    n = len(items)
    
    for i,e in enumerate(items):
        j=1
        while j<n:
            if i >= j:
                left = items[i-j]
            else:
                left = e
                
            if i+j<n:
                right = items[i+j]
            else:
                right=e
                
            if left<e or right<e:
                #new = left if left<right else right
                num.append(min(left,right))
                break
            j+=1
        else:
            num.append(e)
    return num
