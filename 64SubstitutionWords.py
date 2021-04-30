#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:29:03 2020

@author: liweichen
"""

with open('words_sorted.txt', encoding='utf-8') as f:
        words=[x.strip() for x in f]

def substitution_words(pattern, words):
    #tem = []
    vol = []
    
    for word in words:
        if len(word) == len(pattern):
            d1={}
            d2={}
            a=True
            tem=[]
            
            for i in range(len(word)):
                #print(i, Pattern[i])
                tem.append(word[i])
                if tem.count(word[i])>1:
                    #print(word, tem)
                    if d2[word[i]]!=pattern[i]:
                        a=False
                        break
                    else:
                        continue
                if pattern[i] not in d1:
                    #if (d1)
                    d1[pattern[i]] = word[i] #('C': 'a')
                    d2[word[i]] = pattern[i] #('a': 'C' )
                else:
                    if word[i]!=d1[pattern[i]]:
                        a=False
                        break
                    else:
                        continue
                    
            if a==True:
                #print(word, d1)
                vol.append(word)
    return print(vol)
    