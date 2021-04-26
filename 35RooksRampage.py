#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 22:28:43 2020

@author: liweichen
"""


def safe_squares_rooks(n, rooks):
    countrow=0
    countcol=0
    n1=n2=n
    for row in range(n):
        for i in range(len(rooks)):
            if rooks[i][0]==row:
                countrow+=1
                break
    for col in range(n):
        for j in range(len(rooks)):
            if rooks[j][1]==col:
                countcol+=1
                break
    
    n1-=countrow
    n2-=countcol
    return n1*n2
        