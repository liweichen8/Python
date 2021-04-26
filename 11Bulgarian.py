#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:27:35 2020

@author: liweichen
"""


def bulgarian_solitaire(piles, k):
    move = 0
    test = k
    while True:
        count = 0
        if len(piles)>=k:
            for i in range(1,k+1,1):
                if piles.count(i):
                    count += 1
                else:
                    break
        #print(count)
        if count == test:
            break
        num = 0
        move+=1
        for i in range(len(piles)):
            piles[i] = piles[i]-1
            num+=1
        piles.append(num)
        while 0 in piles:
            piles.remove(0)
        #print(piles)
    return move
        
        