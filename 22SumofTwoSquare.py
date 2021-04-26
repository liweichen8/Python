#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 19:34:18 2020

@author: liweichen
"""
import math

def sum_of_two_squares(n):
    i=n
    while i > 0:
        i-=1
        j = n - i
        #print(i,j)
        if math.sqrt(i+1)%1==0 and math.sqrt(j-1)%1==0:
            return (int(math.sqrt(i+1)),int(math.sqrt(j-1)))
        else:
            i = (int(math.sqrt(i)))**2
            #print(i)
    return None