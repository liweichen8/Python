#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 17:56:00 2020

@author: liweichen
"""

'''
def count_distinct_sums_and_products(items):
    list1 = []
    i=0
    nextitems = items
    add = 0
    mul = 0
    if len(items):
        for e in items:
            for j in nextitems:
                add = e+j
                mul = e*j
                if list1.count(add)==0:
                   list1.append(add)
                if list1.count(mul)==0:
                   list1.append(mul)
            i+=1       
            nextitems = items[i:]
        print(len(list1))
    return len(list1)
'''

def count_distinct_sums_and_products(items):
    list1 = []
    i=0
    #nextitems = items
    add = 0
    mul = 0
    if len(items):
        for i in range(len(items)):
            for j in range(i,len(items)):
                add = items[i]+items[j]
                mul = items[i]*items[j]
                if list1.count(add)==0:
                   list1.append(add)
                if list1.count(mul)==0:
                   list1.append(mul)
            #i+=1       
            #nextitems = items[i:]
        #print(len(list1))
    return len(list1)

                