#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 21:19:46 2020

@author: liweichen
"""

import math

def is_cyclops(n):
    if n == 0:
        return True
    else:
        dig = math.ceil(math.log10(n))
        if dig%2 == 0:
            return False
        else:
            exp = int(dig/2)
            new = n//(10**exp)
            print(exp, new)
            if new%10 == 0:
                return True
            else:
                return False