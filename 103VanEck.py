#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 22:32:22 2020

@author: liweichen
"""


def van_eck(n):
    if n < 2:
        return 0
    
    d1 = {0:2}
    prep = {0:0}
    newp = {0:1}
    
    #nextx=0
    prex=0
    
    for i in range(2, n+1):
        if d1[prex]<2:
            nextx=0
            #d1[]+=1
            prep[0]=newp[0]
            newp[0]=i
        else:
            j = prep[prex]
            nextx=i-1-j
            if nextx not in d1:
                d1[nextx]=1
                prep[nextx]=i
            else:
                d1[nextx]+=1
                if d1[nextx]>2:
                    prep[nextx]=newp[nextx]
                newp[nextx]=i
        #print(nextx)
        prex=nextx
    
    return nextx
        