# 4Sum

## Difficulty
Medium

## Pattern
Sorting, Two-pointer concept

## Concepts Used

- Array
- Duplicate Handling 

## Approach

Sort the array.
Fix the first two numbers using two loops.
Use the two-pointer technique to find the remaining two numbers.
Checking if the values at left and right and the fixed element sum up to 0.
If the total is less than 0, left++
If the total is greater than 0, right--
Else, append the combination in answer array and updating the pointers and checking for duplicacy.

## Time Complexity

Sorting = O(n log n)
Outer loop = O(n)
Second loop = O(n)
Two pointers = O(n)
Overall = O(n³)

## Space Complexity

O(1)

## Mistakes I Made

Forgetting to sort the array.
Using incorrect loop ranges (`n-2` instead of `n-3`).
Forgot duplicate values.
Initially solved using nested loops.

## Similar Questions

- 3Sum
- Count Special Quadruplets
- 4Sum II
- 4Sum
- Three Sum
