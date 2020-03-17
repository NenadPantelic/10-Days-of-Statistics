#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:38:12 2020

@author: nenad
"""


# Day 0
# Lecture: https://www.hackerrank.com/challenges/s10-basic-statistics/problem

from collections import Counter
def calculate_basic_params(X):
    # sort the array - beacuse of mode
    X.sort()
    sum = 0
    n = len(X)
    freq = Counter()
    for val in X:
        freq[val] += 1
        sum += val
    mode = X[0]
    mode_freq = freq[mode]
    for val in X:
        if freq[val] > mode_freq:
            mode = val 
            mode_freq = freq[val]
        
    mean = round(sum / n, 1)
    median = round((X[n//2-1] + X[n//2]) / 2,1) if n % 2 == 0 else round(X[n//2],1)
    return (mean, median, float(mode))

N = int(input())
X = list(map(int, input().split()))
#X = [1,2,3,4]
mean, median, mode = calculate_basic_params(X)
print(mean)
print(median)
print(mode)




    
    
    