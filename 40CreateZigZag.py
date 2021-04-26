#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 19:56:49 2020

@author: liweichen
"""


def create_zigzag(rows, cols, start):
    newlist=[]
    for row in range(rows):
        num=[]
        col=1
        #digit = row*cols+start
        if row%2==0:
            ini=row*cols+start
            while col<=cols:
                num.append(ini)
                if col==cols:
                    break
                col+=1
                ini+=1
        else:
            fin=cols+ini
            while col<=cols:
                num.append(fin)
                if col==cols:
                    break
                col+=1
                fin-=1
        #start+=1 
        newlist.append(num)
        print(num, newlist)
    return newlist