#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:18:50 2020

@author: liweichen
"""


def remove_after_kth(items, k):
    new = []
    d1 = {}
    if k == 0:
        return new
    for item in items:
        if item in d1:
            d1[item]+=1
        else:
            d1[item]=1
        if d1[item]<=k:
            new.append(item)
            print(d1[item], new)
    return new
        
    