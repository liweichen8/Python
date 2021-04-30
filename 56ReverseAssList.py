#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:42:51 2020

@author: liweichen
"""


def reverse_ascending_sublists(items):
    num=[]
    res=[]
    i=0
    while len(res)<len(items):
        #print(num, i)
        num.append(items[i])
        if i<len(items)-1:
            while items[i+1]>items[i]:
                num.append(items[i+1])
                print(num, i)
                i+=1
                if i==len(items)-1:
                    break 
        for j in range(len(num)-1,-1,-1):
            res.append(num[j])
        num=[]
        i+=1
        print(res, i)
        if i==len(items):
               break 
        #num=[]
        #i+=1
    return res