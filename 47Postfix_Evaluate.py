#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 22:13:06 2020

@author: liweichen
"""


def postfix_evaluate(items):
    #print(items)
    num=[]
    for i in range(len(items)):
        if type(items[i])==str:
            if items[i]=='+':
                new=num[-2]+num[-1]
            elif items[i]=='-':
                new=num[-2]-num[-1]
            elif items[i]=='*':
                new=num[-2]*num[-1]
            elif items[i]=='/':
                if num[-1]==0:
                    new=0
                else:
                    new=num[-2]//num[-1]
            #print(num[-2], num[-1], new, num)
            num.pop()
            num.pop()
            num.append(new)
            print(num)
            continue
        num.append(items[i])
        #print(num)
    return num[0]