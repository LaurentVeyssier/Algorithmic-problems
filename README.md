# Algorithmic-problems
Resolve a set of problems using appropriate algorithm and design

This project solves a variety of topics related to basic algorithms. The objective is a clean and efficient solution in Python with an explanation of the efficiency of the code and design choices.

- ## Problem 1: Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

  - Design choice: We know that for n> 1 we have sqrt(n) < n. And we are looking for 'a' such as `a <= sqrt(n) < a+1`. This is equivalent to `a^2 <= n < (a+1)^2`. The algorithm is therefore built to identify such 'a' amongst the candidate [0...n-1] for n>1. I follow a divide and conquer strategy similar to binary search with a recursive approach.
    - if the list of candidates contains one element then this element is the solution
    - else choose the central element 'm' in the list of candidates.
    - if m^2 > n then look for the solution is [0...m-1]
    - if n > (m+1)^2 then look for the solution in [m+1,..,n-1]
    - if m^2 <= n < (m+1)^2 then the solution is m
  
  We know that such algorithm is of complexity O(log(n)).
  We can verify this looking at the first elements:
  n _|_ 2 _|_ 3 _|_ 4 _|_ 5

  - Time complexity: All operations have constant time.

  - Space complexity:
