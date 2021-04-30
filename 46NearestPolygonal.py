#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:33:57 2020

@author: liweichen
"""


def nearest_polygonal_number(n, s):
    a=1
    b=2
    num1=((s-2)*(a**2)-(s-4)*a)/2
    num2=((s-2)*(b**2)-(s-4)*b)/2
    while num2<n:
        b=b**2
        num2=((s-2)*(b**2)-(s-4)*b)/2
        #print(num2)
    if num2==n:
        return n
    while b-a>=2:
        mid=(a+b)//2
        num_mid=((s-2)*(mid**2)-(s-4)*mid)/2
        #print(a, b, mid, num_mid)
        if num_mid>n:
            b=mid
            num2=((s-2)*(b**2)-(s-4)*b)/2
        else:
            a=mid
            num1=((s-2)*(a**2)-(s-4)*a)/2
    #print(a, b, num1, num2)
    if n-num1<=num2-n:
        return num1
    elif n-num1>num2-n:
        return num2
        