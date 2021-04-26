#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:26:09 2020

@author: liweichen
"""


def count_and_say(digits):
    if digits == '':
        return ''
    
    num = ''
    index = digits[0]
    count = 1
    
    for c in digits[1:]:
        if c != index:
            num += str(count) + index
            count=1
            index=c
        else:
            count+=1
            
    num += str(count) + index
    return num
            