#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 22:28:44 2020

@author: liweichen
"""


from fractions import Fraction
from collections import deque

def calkin_wilf(n):
    i=1
    f = Fraction(1,1)
    seq = deque()
    seq.append(f)
    while i<n:
        #print(seq, seq[0])
        num = seq.popleft()
        #print(num.numerator)
        p = num.numerator
        q = num.denominator
        first = Fraction(p,p+q)
        second = Fraction(p+q,q)
        seq.append(first)
        i+=1
        if i==n:
            return seq.pop()
        seq.append(second)
        i+=1
        if i==n:
            return seq.pop()
        
        