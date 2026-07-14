# Move Zeroes

## Difficulty
Easy

## Pattern
Two-pointer concept

## Concepts Used

- Array
- Two-pointer concept
 

## Approach

Use two-pointer technique.
Use left to shift the non-zero elements in the array, and right to access the current element. 
If the element at index right is non-zero then swap the elemnent with the element on left; and increment left.
Return nums

## Time Complexity

Overall = O(n)

## Space Complexity

O(1)

## Mistakes I Made

Forgot to shift the left pointer.

## Similar Questions

-Remove Element
-Apply Operations to an Array
-Maximum Tastiness of Candy Basket
-House Robber IV
