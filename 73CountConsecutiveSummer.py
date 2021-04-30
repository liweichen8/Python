#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 23:01:44 2020

@author: liweichen
"""


def count_consecutive_summers(n):
    i=1
    count=0
    while i<=n:
        if n%i==0:
            count+=1
        i+=2
    return count