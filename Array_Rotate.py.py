#!/usr/bin/env python
# coding: utf-8

# <b>Array Rotate: </b> <i>Shifting Elements </i>
# 
# <b>Problem Source:</b>  https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0

# In[1]:


# n is the array and k is the number of positions to shift

def arr_rot(n, k):
    counter = 0
    while counter < k:
        temp = n.pop(0)
        n.append(temp)
        counter += 1
    return n


# In[2]:


# Inputs

a = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
shifts = 3
print(arr_rot(a,shifts))


# In[ ]:




