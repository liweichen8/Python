#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 22:19:02 2020

@author: liweichen
"""


def recaman(n):
    Reseq = [1]
    s = {1}
    for i in range(1,n):
        #print(Reseq[i-1]-(i+1), Reseq, s)
        if Reseq[i-1]-(i+1)>0 and (Reseq[i-1]-(i+1)) not in s: 
            Reseq.append(Reseq[i-1]-(i+1))
            s.add(Reseq[i-1]-(i+1))
        else:
            Reseq.append(Reseq[i-1]+(i+1))
            s.add(Reseq[i-1]+(i+1))
    return Reseq[-5:]



"""
def recaman(n):
    Reseq = [1]
    for i in range(1,n):
        #print(Reseq[i-1]-(i+1), Reseq, s)
        if Reseq[i-1]-(i+1)>0 and (Reseq[i-1]-(i+1)) not in Reseq: 
            Reseq.append(Reseq[i-1]-(i+1))        
        else:
            Reseq.append(Reseq[i-1]+(i+1))        
    return Reseq[-5:]
"""