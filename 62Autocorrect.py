#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:25:23 2020

@author: liweichen
"""

'''
def autocorrect_word(word, words, df):
    correct = ''
    safe = 10000
    
    for w in words:
        if len(w)==len(word):
            s = 0
            for i in range(len(w)):
                s += safe(w[i], word[i])
                if s < safe:
                    safe=s
                    correct=w
    return correct
'''


def autocorrect_word(word, words, df):
     correct = ''
     bd = 10000
     
     for w in words:
         if len(w)==len(word):
             d=0
             for c1, c2 in zip(w, word):
                 d+=df(c1,c2)
                 if d<bd:
                    bd=d
                    correct=w
     return correct