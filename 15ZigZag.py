#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:52:21 2020

@author: liweichen
"""


def is_zigzag(n):
    num = str(n)
    if len(num) < 2:
        return True
    else:
        for i in range(len(num)-2):
            diff1 = int(num[i+1]) - int(num[i])
            diff2 = int(num[i+2]) - int(num[i+1])
            print(diff1, diff2)
            if diff1*diff2 >= 0:
                return False
        return True