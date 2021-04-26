#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 17:03:53 2020

@author: liweichen
"""


def tukeys_ninthers(items):
    median = 0
    newlist = []
    while len(items) > 1:
        for i in range(len(items)):
            if (i+1) % 3 == 0:
                if items[i-2]>items[i-1] and items[i-2]>items[i]:
                    median = max(items[i-1],items[i])
                elif items[i-2]<items[i-1] and items[i-2]<items[i]:
                    median = min(items[i-1],items[i])
                else:
                    median = items[i-2]
                newlist.append(median)
        print(newlist)
        items = newlist
        newlist = []
    return items[0]
                
        