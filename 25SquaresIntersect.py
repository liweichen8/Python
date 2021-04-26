#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:54:50 2020

@author: liweichen
"""


def squares_intersect(s1, s2):
    end1 = (s1[0]+s1[2],s1[1]+s1[2])
    end2 = (s2[0]+s2[2],s2[1]+s2[2])
    if min(end1[0],end2[0]) < max(s1[0],s2[0]):
        return False
    if min(end1[1],end2[1]) < max(s1[1],s2[1]):
        return False
    return True