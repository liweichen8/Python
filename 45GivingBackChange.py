#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 21:55:10 2020

@author: liweichen
"""


def give_change(amount, coins):
    total=0
    addup = []
    for i in range(len(coins)):
        while total+coins[i] <= amount:
            total+=coins[i]
            addup.append(coins[i])
        print(total, addup)
    return addup