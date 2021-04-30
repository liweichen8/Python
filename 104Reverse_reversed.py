#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 22:59:19 2020

@author: liweichen
"""


def reverse_reversed(items):
    for i in range(len(items)):
        if type(items[i])==list:
            #print(items[i])
            item=reverse_reversed(items[i])
            items[i]=item
            #print(items[i], item)
    return items[::-1]