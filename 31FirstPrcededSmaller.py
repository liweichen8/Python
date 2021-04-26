#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 18:01:44 2020

@author: liweichen
"""


def first_preceded_by_smaller(items, k):
    for i in range(len(items)):
        count=0
        num = items[:i]
        for j in range(len(num)):
            if num[j]<items[i]:
                count+=1
            if count==k:
                return items[i]
    return None
            