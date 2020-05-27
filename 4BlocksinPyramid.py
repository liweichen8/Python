#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 21:10:27 2020

@author: liweichen
"""


def pyramid_blocks(n,m,h):
    blocks = 0
    for x in range(h):
        num = (n+x) * (m+x)
        blocks += num
    return blocks
        