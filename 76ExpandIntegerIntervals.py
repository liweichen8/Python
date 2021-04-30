#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:36:46 2020

@author: liweichen
"""


def expand_intervals(intervals):
    num = []
    items = intervals.split(',')
    
    for i in items:
        parts = i.partition('-')
        if parts[1] == '-':
            ini = int(parts[0])
            fin = int(parts[2])
        else:
            ini = int(parts[0])
            fin = ini
        
        num.extend(range(ini, fin+1))
        
    return num