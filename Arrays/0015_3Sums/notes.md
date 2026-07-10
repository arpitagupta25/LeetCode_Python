# 3Sum

## Difficulty
Medium

## Pattern
Sorting, Two-pointer concept

## Concepts Used

- Array
- Duplicate Handling 

## Approach

Sorting the num array.
Fixing the first element.
Using two pointers (left and right) given left<right:
Checking if the values at left and right and the fixed element sum up to 0.
If the total is less than 0, left++
If the total is greater than 0, right--
Else, append the combination in answer array and updating the pointers and checking for duplicacy.

## Time Complexity

- Sorting: O(n log n)
- Outer loop: O(n)
- Two-pointer search: O(n)

## Space Complexity

O(1)

## Mistakes I Made

Forgot duplicate values.
Initially solved using nested loops.

## Similar Questions

- 3Sum Closest
- 4Sum
- Number of arithmetic triplets
- 4Sum
- Three Sum
