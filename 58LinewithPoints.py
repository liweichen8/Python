#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:10:03 2020

@author: liweichen
"""


def cross(p1, p2, p3):
    (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


#print(cross((7,3), (7,1), (7,4)))


def line_with_most_points(points):
    if len(points)<3:
        return len(points)
    else:
        count=2
        big=0
        for i in range(0,len(points)-2):
            for j in range(i+1, len(points)-1):
                for k in range(j+1, len(points)):
                    #print(points[i],points[j],points[k])
                    if cross(points[i],points[j],points[k])==0:
                        count+=1
                if count>big:
                    big=count
                count=2
        return big