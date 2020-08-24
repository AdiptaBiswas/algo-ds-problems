#!/usr/bin/env python
# coding: utf-8

# Binary Search and Linear Search on a large number along with Time

import time
 
# Binary Search 

def binary_search(given_list,item):
    start = time.time()
    low = 0
    high = len(given_list)-1
    mid = (low + high) // 2
    while given_list[mid] != item:
        if given_list[mid]<item:
            low=mid+1
            mid=(low+high) // 2
        elif given_list[mid] == item:
            return "{} matched at {}".format(item,mid), time.time() - start
        else:
            high=mid-1
            mid=(low+high) // 2
    return "{} matched at {}".format(item,mid), time.time() - start  

list_n = [x for x in range(10000000)]
Output, Time = binary_search((list_n),622253)
print(Output)
# 622253 matched at 622253

print()
print("It took {:.8f} milliseconds to search".format(Time))

# It took 0.00000000 milliseconds to search


# Linear Search

def linear_search(given_list,item):
    start = time.time()
    for num in given_list:
        if num == item:
            return "{} matched at {}".format(item,given_list.index(num)), time.time() - start

list_n = [x for x in range(10000000)]
Output, Time = linear_search(list_n,622253)
print(Output)
# 622253 matched at 622253

print()
print("It took {:.8f} milliseconds to search".format(Time))
# It took 0.04587674 milliseconds to search






