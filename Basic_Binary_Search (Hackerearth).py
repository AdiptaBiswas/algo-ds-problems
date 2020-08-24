#!/usr/bin/env python
# coding: utf-8

# <b>Search Algorithm:</b> <i>Binary Search </i>
# 
# <b>Problem Source:</b>  https://www.hackerearth.com/practice/algorithms/searching/binary-search/tutorial/


def binary_search(length,number,given_list):
    low = 0
    high = length-1
    mid = (low+high)//2
    while given_list[mid]!=number:
        if given_list[mid] == number:
            return mid
        elif given_list[mid] < number:
            low = mid+1
            mid = (low+high)//2
        else:
            high = mid-1
            mid = (low+high)//2
    return mid

N = int(input("Array size: "))
print(N)
List = []
for i in range(N):
    numb = int(input("Enter the elements: "))
    List.append(numb)
print(List)
q = int(input("Enter the number of queries: "))
for i in range(q):
    element = int(input("Enter: "))
    print("{} is in {}th position in List".format(element, binary_search(N,element,List)))
    
    
'''Array size: 10
10
Enter the elements: 1
Enter the elements: 2
Enter the elements: 3
Enter the elements: 4
Enter the elements: 5
Enter the elements: 6
Enter the elements: 7
Enter the elements: 8
Enter the elements: 9
Enter the elements: 10
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Enter the number of queries: 2
Enter: 7
6
Enter: 2
1
'''




