#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:54:28 2020

@author: liweichen
"""


def hitting_integer_powers(a, b, tolerance = 100):
    ax, bx, aa, bb = 1, 1, a, b
    while tolerance * abs(aa-bb) > min(aa,bb):
        if aa<bb:
            aa, ax = aa*a, ax+1
        else:
            bb, bx = bb*b, bx+1
    return (ax, bx)