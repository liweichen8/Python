#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 18:28:37 2020

@author: liweichen
"""


def frequency_sort(elems):
    d1={}
    sort=[]
    res=[]
    elems=sorted(elems)
    print(elems)
    
    for num in elems:
        if num not in d1:
            sort.append(num)
            d1[num]=1
            continue
        d1[num]+=1
    
    sort_d1=sorted(d1.items(), key=lambda x: x[1], reverse=True)
    print(sort_d1)
    
    for i in range(len(sort_d1)):
        for j in range(sort_d1[i][1]):
            res.append(sort_d1[i][0])            
    
    return res

