#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 21:50:32 2020

@author: liweichen
"""


def reverse_vowels(text):
    letter=[]
    st = 'aeiouAEIOU'
    for c in text:
        if c in st:
            letter.append(c)
    #print(letter)
    textlist = list(text)
    l=len(letter)
    for i in range(len(textlist)):
        if textlist[i] in st:
            l-=1
            #print(l, textlist)
            if textlist[i].isupper():
                textlist[i] = letter[l].upper()
            else:
                textlist[i] = letter[l].lower()
    return ''.join(textlist)
            