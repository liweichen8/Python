#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:16:55 2020

@author: liweichen
"""


def words_with_letters(words,letters):
    subseq = []
    for line in words:
        y=0
        i=0
        #line=words.readline()
        #line='azotetrazole'
        for l in letters:
            for x in range(y,len(line)):
                if line[x]==l:
                    i+=1
                    y=x+1
                    #print(i,y,l,line[x],line)
                    break
        if i == len(letters):
            line=line.replace('\n','')
            print(line)
            subseq.append(line)
    return subseq
                    
    #words.close()