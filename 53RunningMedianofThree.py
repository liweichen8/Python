#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 19:22:10 2020

@author: liweichen
"""


def running_median_of_three(items):
    newlist=[]
    median=0
    i=2
    if len(items)<3:
        return items
    else:
        newlist.append(items[0])
        newlist.append(items[1])
        while len(items)>2 and i<len(items):
            if items[i-2]>items[i-1] and items[i-2]>items[i]:
                median = max(items[i-1],items[i])
            elif items[i-2]<items[i-1] and items[i-2]<items[i]:
                median = min(items[i-1],items[i])
            else:
                median = items[i-2]
            newlist.append(median)
            print(items, newlist, median)
            i+=1
    return newlist