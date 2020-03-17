#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:54:29 2020

@author: nenad
"""
# Lesson: https://www.hackerrank.com/challenges/s10-weighted-mean/problem

def weighted_mean(X,W):
    sum_num, sum_denum = 0,0
    for i in range(len(X)):
        sum_num += X[i] * W[i]
        sum_denum += W[i]
    return round(sum_num / sum_denum, 1)


N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))
print(weighted_mean(X, W))
    