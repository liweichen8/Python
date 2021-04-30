#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 22:59:48 2020

@author: liweichen
"""


def get_emp(hand):
    #suits = ['spades', 'hearts', 'diamonds', 'clubs']
    ranks = {'deuce': 2, 'trey': 3, 'four': 4, 'five': 5, 'six': 6,
         'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
         'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}
    emp=[]
    for card in hand:
        name = {'Suit': card[1], 'num': card[0], 'value': ranks[card[0]]}
        emp.append(name)
    
    emp.sort(key=get_value, reverse=True)
    #print(emp)
    return emp
    
def get_value(emp):
    return emp.get('value')


def bridge_hand_shorthand(hand):
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    ranks = {'deuce': 2, 'trey': 3, 'four': 4, 'five': 5, 'six': 6,
         'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,}
    
    high = {'jack': 'J', 'queen': 'Q', 'king': 'K', 'ace': 'A'}
    #letter=['AKQJ']
    card=[]
    emp = get_emp(hand)
    print(emp)
   
    
    for suit in suits:
        #suitcard=[]
        count=0
        for cards in emp:
            if cards.get('Suit')==suit:
                count+=1
                if cards.get('num') in ranks:
                    #suitcard.append('x')
                    card.append('x')
                elif cards.get('num') in high:
                    h = high[cards.get('num')]
                    #suitcard.append(h)
                    card.append(h)
        #card.append(suitcard)
        if count==0:
            card.append('-')
        if suit=='clubs':
            break
        card.append(' ')
        
    card=''.join(card)
    
    return card
                
    
    
    
    
    