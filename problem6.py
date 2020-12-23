# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 01:25:54 2020

@author: lveys
"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints)==0:
        return None
    
    if len(ints)==1:
        return (ints[0],ints[0])
    
    # initialize containers for min and max elements
    minimum = None
    maximum = None
    
    # Traverse the list and store min and max elements
    for n in ints:
      
        if minimum is None:
          minimum = n
        # always keep the lowest element discovered
        elif n < minimum:
          minimum = n
    
        if maximum is None:
          maximum = n
        # always keep the highest element discovered
        elif n > maximum:
          maximum = n
    
    return (minimum, maximum)
          
    

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [0]  # a list containing 0
random.shuffle(l)
print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail")

l = []  # a list containing nothing
print ("Pass" if (None == get_min_max(l)) else "Fail")