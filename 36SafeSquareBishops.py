#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 21:48:11 2020

@author: liweichen
"""


def safe_squares_bishops(n, bishops):
    occ = bishops[:]
    for point in bishops:
        for x in range(n):
            #print(point, occ, x, point[0]!=x)
            if point[0]!=x:
                #print(point, occ, x, point[0]!=x)
                for y in range(n):
                    if point[1]!=y:
                        #print(point, occ, y, point[1]!=y)
                        if abs(x-point[0])==abs(y-point[1]) and (x,y) not in occ:
                            occ.append((x,y))
                            #print(occ)
    #print(occ)
    num = n*n - len(occ)
    return num