#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 22:18:48 2020

@author: liweichen
"""


from fractions import Fraction

def kempner(n):
    kemp = 0
    for i in range(1,n+1):
        f = str(i)
        if f.count('9'):
            continue
        print(Fraction(1,i))
        kemp+=Fraction(1,i)
    kemp = kemp.limit_denominator(1000)
    return kemp