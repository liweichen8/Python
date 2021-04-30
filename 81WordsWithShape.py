#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 17:49:45 2020

@author: liweichen
"""


def words_with_given_shape(words, shape):
    num=0
    result=[]
    for line in words:
        check=[]
        if len(line) == len(shape)+2:
            line=line.replace('\n','')
            #print(line)
            for i in range(len(line)-1):
                if line[i+1]>line[i]:
                    num=1
                elif line[i+1]<line[i]:
                    num=-1
                else:
                    num=0
                check.append(num)
            if check == shape:
                result.append(line)
    return result
                
         
            