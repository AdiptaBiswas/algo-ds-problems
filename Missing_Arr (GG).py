#!/usr/bin/env python
# coding: utf-8

# <b>Search Algorithm O(n):</b> <i>Missing Array </i>
# 
# <b>Problem Source:</b>  https://practice.geeksforgeeks.org/problems/missing-number-in-array/0#ExpectOP

# In[ ]:


def Missing(Arr,N):
    print("{}".format(sum(list(range(1,N+1))) - sum(Arr[:])))

    
T = int(input())
for i in range(T):
    N = int(input())
    Arr = [int(num) for num in input().split()]
    Missing(Arr,N)

