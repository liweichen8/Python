#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 21:48:51 2020

@author: liweichen
"""


def is_ascending(items):
    n = len(items)
    if n <= 1:
        return True
    else:
        items.append(0)
        for x in range(n):
            print(x)
            if items[x+1] - items[x] <= 0:
                break  
        if x == n-1:
            return True
        else:
            return False


"""
for n in range(0,3,1):
    print(n)
print("hello")
"""
  