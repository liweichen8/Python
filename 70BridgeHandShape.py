#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:15:10 2020

@author: liweichen
"""


def bridge_hand_shape(hand):
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    shape=[]
    #count=0
    
    for suit in suits:
        count=0
        for card in hand:
            #print(card, card[1], card[1]==suits, )
            if card[1]==suit:
                count+=1
        shape.append(count)
        
    return shape
        
    