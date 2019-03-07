#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 13:19:27 2018

@author: liyunqiu
"""
#Yunqiu Li
#Assignment 1
#Exercise 3


def function_sum_xsquare(valueSet):
    total = 0 
    for pair in valueSet:
        xi = pair[0]
        total  += xi**2
    return total
    
def function_sum_x(valueSet):
    total = 0 
    for pair in valueSet:
        xi = pair[0]
        total += xi
    return total
    
def function_sum_xy(valueSet):
    total = 0
    for pair in valueSet:
        xi = pair[0]
        yi = pair[1]
        total += xi*yi
    return total

def function_sum_y(valueSet):
    total = 0
    for pair in valueSet:
        yi = pair[1]
        total += yi
    return total
        
#list of (xi,yi)
valueSet = [(1,2),(3,4),(5,6),(7,8),(9,10)]
print("input (xi,yi) value set is: ")
print(valueSet)

n = len(valueSet)
sumX = function_sum_x(valueSet)
sumY = function_sum_y(valueSet)
sumXSquare = function_sum_xsquare(valueSet)
sumXY = function_sum_xy(valueSet)

divider = sumX**2 - n*sumXSquare
a = (sumXY*sumX - sumY*sumXSquare)/divider
b = (sumY* sumX - n*sumXY)/divider

print("a =" + str(a))
print("b =" + str(b))
