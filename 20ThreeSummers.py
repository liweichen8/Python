#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:10:33 2020

@author: liweichen
"""


def two_summers(items, goal, i = None, j = None):
    i = i if i else 0
    j = j if j else len(items) - 1
    while i < j:
        x = items[i] + items[j]
        if x == goal:
            return True
        elif x < goal:
            i += 1
        else:
            j -= 1
    return False


def three_summers(items, goal):
    n = len(items)
    for i in range(n):
        three = items[:]
        
        del(three[i])
        
        if two_summers(three, goal-items[i]):
            return True
    
    return False