#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:47:13 2020

@author: liweichen
"""


def possible_words(words, pattern):
    word = []
    
    for w in words:
        if len(w) == len(pattern):
            for (chw, chp) in zip(w, pattern):
                if chp != '*' and chp != chw:
                    break
                if chp == '*' and chw in pattern:
                    break
            else:
                word.append(w)
    return word