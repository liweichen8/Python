#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:54:35 2020

@author: liweichen
"""


def josephus(n, k):
    order = []
    men = list(range(1,n+1))
    count=0
    while men:
        for i in range(k):
            count+=1
            if count>len(men):
                count=1       
        count-=1
        order.append(men[count])
        men.remove(men[count])
        #print(count, men, len(men))
        if count>=len(men):
            count=0
            #print('hello', count, len(men))
            #continue
        #count-=1
    return order