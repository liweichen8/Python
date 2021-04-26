#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:07:12 2020

@author: liweichen
"""


def group_and_skip(n, out, i):
    taken = []
    while n:
        rem = n%out
        groups = (n-rem)/out
        taken.append(int(rem))
        n = i*groups
    return taken