#!/usr/bin/env python
# coding: utf-8

# <b>Array Rotate: </b> <i>Shifting Elements </i>
# 
# <b>Problem Source:</b>  https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0

# n is the array and k is the number of positions to shift

def arr_rot(n, k):
    counter = 0
    while counter < k:
        temp = n.pop(0)
        n.append(temp)
        counter += 1
    return n

# Inputs

a = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
shifts = 3
print(arr_rot(a,shifts))

# [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]

------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

# <b>Array Rotate: </b> <i>Cyclic Shifting Elements </i>
#
# <b>Problem Source:</b>  https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one/0

# arr is the array

def cycle_Arr(arr):
    count = 0
    while count < len(arr)-1:
        temp = arr.pop(0)
        arr.append(temp)
        count += 1
    return arr

# Inputs

a = [9, 8, 7, 6, 4, 2, 1, 3]
print(cycle_Arr(a))

# [3, 9, 8, 7, 6, 4, 2, 1]

