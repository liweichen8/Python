#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:56:12 2020

@author: liweichen
"""


def taxi_zum_zum(moves):
    x = 0
    y = 0
    arrow = 0
    #direc = [0,1,2,3]
    turn = list(moves)
    for i in range(len(turn)):
        if turn[i] == 'L':
            arrow -= 1
            if arrow == -1:
                arrow = 3
        elif turn[i] == 'R':
            arrow += 1
            if arrow == 4:
                arrow = 0
        elif turn[i] == 'F':
            if arrow == 0:
                y+=1
            elif arrow == 1:
                x+=1
            elif arrow == 2:
                y-=1
            else:
                x-=1
    return (x,y)
                
    