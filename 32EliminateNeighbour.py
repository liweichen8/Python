#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 18:57:43 2020

@author: liweichen
"""


def eliminate_neighbours(items):
    #print(items)
    count=0
    n=len(items)
    #data=items[:]
    if len(items)<3:
        return 1
    for num in range(1,n+1):
    #while num == min(items):
        for i in range(len(items)):
            print('hello', i, items[i], num)
            if items[i]==num:
                count+=1
                if len(items)>1: 
                    if i==0:
                        items.remove(items[i+1])
                    elif i==(len(items))-1:
                        items.remove(items[i-1])
                    else:
                        left=items[i-1]
                        right=items[i+1]
                        items.remove(max(left,right))
                items.remove(num)
                print(num, items, len(items))
                break
        if items.count(n)==0:
            break
    return count
