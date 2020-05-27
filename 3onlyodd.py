#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:07:32 2020

@author: liweichen
"""


def only_odd_digits(n):
    b = len(str(n))
    for x in range(1,b+2,1):
        num = n//(10**(b-x))
        print(x, num)
        if num%2 == 0:
            break
    if x <= b:
        return False
    else:
        return True
    

        
    