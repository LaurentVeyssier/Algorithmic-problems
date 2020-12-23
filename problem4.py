# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 01:49:16 2020

@author: lveys
"""

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list==[]:
        return []
    
    length = len(input_list)
    
    # prepare container filled with 1. We will replace by 0 or 2 as required
    sorted_list = [1] * length
    
    # initialize index to insert 0 and 2 on the left and right sides
    left_index = 0
    right_index = length-1
    
    # traverse the input list and insert 0 or 2 appropriately
    for input in input_list:
        if input ==0:
            sorted_list[left_index] = 0
            left_index+=1
        elif input ==2:
            sorted_list[right_index] = 2
            right_index-=1
    
    return sorted_list
    

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
test_function([0])