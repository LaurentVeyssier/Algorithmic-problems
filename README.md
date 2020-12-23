# Algorithmic-problems
Resolve a set of problems using appropriate design for most efficient algorithm.

This project solves a variety of topics related to basic algorithms. The objective is a clean and efficient solution in Python with an explanation of the efficiency of the code and design choices.

## Problem 1: Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

  - Design choice: We know that for n> 1 we have sqrt(n) < n. And we are looking for 'a' such as `a <= sqrt(n) < a+1`. This is equivalent to `a^2 <= n < (a+1)^2`. The algorithm is therefore built to identify such 'a' amongst the candidate [0...n-1] for n>1. I follow a divide and conquer strategy similar to binary search with a recursive approach.
    - if the list of candidates contains one element then this element is the solution
    - else choose the central element 'm' in the list of candidates.
    - if m^2 > n then look for the solution is [0...m-1]
    - if n > (m+1)^2 then look for the solution in [m+1,..,n-1]
    - if m^2 <= n < (m+1)^2 then the solution is m
  
  for n = 0 we have 0 and for n = 1 we have 1.
  
  - Time complexity:
  We know that such algorithm is of complexity O(log(n)).
  We can verify this looking at the first elements:
  
![](asset/sqrt.jpg)
  
  so we have roughly for 2^k < n < 2^(k+1), k iterations on average. This indicates a complexity of O(log(n)).

  - Space complexity: O(n) since we use a list of candidates of size n




## Problem 4: Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.
 
 - Design choice: Since we have only 3 classes (0,1,2), we can easily insert the 0 and 2 at the extremities but lack information on 1 since we must sort in a single pass.
 I choose to prefill an array with '1's and will replace with 0 or 2 appropriately on the extremities while traversing the unsorted array.
 
  - Time complexity: Since we traverse the list only once to return the solution, the complexity is O(n).
  
  - Space complexity: O(n) since we store the solution in a list of same size as the input.



## Problem 6: Max and Min in a Unsorted Array
Look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

  - Design choice: Sorting would allow to identify the lowest and highest elements. However I will not sort the list as this takes O(nlog(n)). I choose to traverse the list once and store the lowest and highest elements as we go through each element of the list.
  
  - Time complexity: Since we traverse the list only once to return the solution, the complexity is O(n). This is more efficient as sorting since we do not have to sort all the elements.
  
  - Space complexity: This algorithm has constant space. It does not change based on the size of the array.
