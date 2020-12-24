# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 00:57:23 2020

@author: lveys
"""

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    
    # Perform MergeSort to sort the input list - O(nlog(n))
    def merge(left, right):
        
        merged = []
        left_index = 0
        right_index = 0
        
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                merged.append(right[right_index])
                right_index += 1
            else:
                merged.append(left[left_index])
                left_index += 1
    
        merged += left[left_index:]
        merged += right[right_index:]
            
        return merged
    
    def mergesort(items):

        if len(items) <= 1:
            return items
        
        mid = len(items) // 2
        left = items[:mid]
        right = items[mid:]
        
        left = mergesort(left)
        right = mergesort(right)
        
        return merge(left, right)
    
    output_list = mergesort(input_list)
    print(output_list)
    
    # Assemble the solution O(n)
    # Initialize containers for the two numbers
    output_1 = ''
    output_2 = ''
    # Build the 2 solutions by distributing alternatively the digits from largest to smallest
    # The number of digits in both solution numbers cannot differ by more than 1 (equal if list has even number of elements)
    for i in range(len(output_list)-1, -1, -1):
        if i%2==0:
            output_1+=str(output_list[i])
        else:
            output_2+=str(output_list[i])
    
    return [int(output_1), int(output_2)]
    

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])