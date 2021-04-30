#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:26:52 2020

@author: liweichen
"""


from fractions import Fraction

def fractran(n, prog, giveup=20):
    new = []
    i=1
    l=False
    new.append(n)
    if not prog:
        return new
    while i<=giveup:
        for num in prog:
            newnum = n*Fraction(num[0],num[1])
            if newnum%1==0:
                new.append(int(newnum))
                n=int(newnum)
                #num=prog[0]
                i+=1
                l=True
                break
        if l==False:
            break
        l=False
    return new
            