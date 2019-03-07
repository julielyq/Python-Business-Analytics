#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 11:59:01 2018

@author: liyunqiu
"""
#Yunqiu Li
#Assignment 1

#Exercise 1

k = int(input("What is the value of k? "))
     

def equation(k):
    return k*(k+1)/2 + (k+1)
     
while (k <= 0):
    print("k is not valid. Please enter a postivie integer.")
    k = int(input("What is the value of k? "))
        
print("Right side is equal to " + str(int(equation(k))))
right_side = equation(k)

# it is k+2 because of range index
integer_list = range(1,k+2)
left_side = sum(integer_list)
print("Left side is equal to " + str(left_side))

if right_side == left_side:
    print("Equation is true for any positive integer k.")
else:
    print("Equation is not true for any positive integer k.")
