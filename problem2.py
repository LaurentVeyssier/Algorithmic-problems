# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 02:52:52 2020

@author: lveys
"""

def rotated_array_search_sln(input_list, number, start_index, end_index):
    
    # necessary condition to calculate the mid index
    if start_index > end_index:
        return -1
    
    # Calculate mid index of the list for binary search
    mid = (start_index+end_index)//2
    
    # base case
    if input_list[mid]==number:
        return mid
    
    # we recursively perform binary search on ordered segments
    # check if the left segment is ordered <=> mid index is before the random pivot
    if (input_list[start_index] <= input_list[mid]):
        # check if target number is within this segment on pivot left side
        if (input_list[start_index] <= number < input_list[mid]):
            # if target number is within segment, recursive search on that segment
            return rotated_array_search_sln(input_list, number, start_index, mid-1)
        else:
            # if target is not in segment, then back to initial problem: search reduced list which includes pivot
            return rotated_array_search_sln(input_list, number, mid+1, end_index)
    # if mid index is after the random pivot then the ordered segment starts from mid index to the right 
    elif (input_list[start_index] > input_list[mid]):
        # if target outside that segment, recursive search segment right of mid index
        if input_list[mid] < number <= input_list[end_index]:
            return rotated_array_search_sln(input_list, number, mid+1, end_index)
        # if target outside that segment, then back to initial problem: search reduced list which includes pivot
        else:
            return rotated_array_search_sln(input_list, number, start_index, mid-1)
    

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    
    return rotated_array_search_sln(input_list, number, 0, len(input_list)-1)
        


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[4,5,6,7,0,1,2], 0])