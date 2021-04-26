#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:42:08 2020

@author: liweichen
"""


def double_until_all_digits(n, giveup = 5):
    count = 0
    time = 0
    while count < 10:
        num = str(n)
        for i in range(10):
            for j in range(len(num)):
                if num[j]==str(i):
                    count+=1
                    break
        if count<10:
            n = n*2
            time+=1
            print(n,count)
            count=0
        if time==giveup:
            return -1
    return time