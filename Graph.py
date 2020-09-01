# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 22:18:22 2020

@author: Saptarshi
"""

M, N = [int(i) for i in input().split()]

def largest_factor(n):
    a = int(n/2)+1
    for i in range(2,a):
        if n%i ==0:
            return int(n/i)
    return 1

max = max(M,N)
min = min(M,N)

if M==N:
    print(0)
    
else:
    a = []
    b=()
    a.append(M)
    a.append(N)
    flag = 0
    while max!=1:
        factor = largest_factor(max)
        a.append(factor)
        if factor == min:
            flag = 1
            b = set(a)
            print(len(b)-1)
            break
        max = factor
    
    while min!=1 and flag==0:
        factor = largest_factor(min)
        a.append(factor)
        
        min = factor
        
    if flag == 0:
        
        b = set(a)
        print(len(b)-1)