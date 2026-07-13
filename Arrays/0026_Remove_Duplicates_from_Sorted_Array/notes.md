# Remove Duplicates From Sorted Array

## Difficulty
Easy

## Pattern
Two-pointer concept

## Concepts Used

- Array
- Two-pointer concept
- Duplicate Handling 

## Approach

Use two-pointer technique.
Use k to update the unique elemnts in the array, and i to access the current element. 
Check if the array is empty, if yes return 0.
Else, if index is 0, increment both i and k.
If the element at index i and i-1 are same, increment i.
Else, update nums[k]=nums[i] and increment i and k.
Return k

## Time Complexity

Overall = O(n)

## Space Complexity

O(1)

## Mistakes I Made

Didnot update the array with unique elemnts and later duplicate elements.
Didnot consider the empty array case.


## Similar Questions

-Remove Element
-Remove Duplicates from Sorted Array II
-Apply Operations to an Array
-Sum of Distances
-Maximum Tastiness of Candy Basket
-House Robber IV
