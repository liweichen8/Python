#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:04:50 2020

@author: liweichen
"""


def is_palindrome(word):
    return word==word[::-1]


def longest_palindrome(text):
    test = is_palindrome(text)   
    if test==True:
            return text
    copy=text
    ran=len(copy)-1      

    while test==False:
       i=0
       while ran<=len(text):
           copy = text[i:ran]
           #print(i,ran,copy)
           test = is_palindrome(copy)
           if test==True:
               return copy
           i+=1
           ran+=1
       ran=len(copy)-1
       if ran<3:
           break