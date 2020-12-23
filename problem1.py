# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 23:05:50 2020

@author: lveys
"""

def sqrt_sln(number, arr):
    # Note: using floor, there will always be a solution to the problem
    
    # if the list of candidates has only one element, this is the solution
    if len(arr)<=1:
        return arr[0]
    
    # pick middle of the list
    mid = len(arr) //2
    
    # we look for a such as : a^2 <= n < (a+1)^2
    # if a^2 > n then look for solution in left part of the list
    if arr[mid]*arr[mid] > number:
        return sqrt_sln(number, arr[:mid])
    # if n >= (a+1)^2 then look for solution in right part of the list
    if number >= (arr[mid]+1)*(arr[mid]+1):
        return sqrt_sln(number, arr[mid+1:])
    # else we found the solution a
    return arr[mid]


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        print('you must enter a positive integer')
        return -1
    if number ==0:
        return 0
    if number ==1:
        return 1
    
    # the candidate is an integer 'a' such as: a <= sqrt(n) < n
    # the list of candidates is within [0...n-1]
    candidates = [_ for _ in range(number)]
    
    return sqrt_sln(number, candidates)



print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (12 == sqrt(152)) else "Fail")
print ("Pass" if  (38 == sqrt(1520)) else "Fail")
print ("Pass" if  (1 == sqrt(2)) else "Fail")
print ("Pass" if  (-1 == sqrt(-1)) else "Fail")