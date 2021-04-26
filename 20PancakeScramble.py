#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 22:29:05 2020

@author: liweichen
"""


def pancake_scramble(text):
    i = 0
    text = list(text)
    word = list(text)
    for n in range(1,len(text)):
        for j in range(n,-1,-1):
            text[i] = word[j]
            #print(i,j,text,word)
            i+=1
        i=0
        for x in range(len(text)):
            word[x] = text[x]
        #print(text)
    return ''.join(text)