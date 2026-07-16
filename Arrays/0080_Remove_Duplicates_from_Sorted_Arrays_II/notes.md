# Remove Duplicates From Sorted Array II

## Difficulty
MEdium

## Pattern
Two-pointer concept

## Concepts Used

- Array
- Two-pointer concept
- Duplicate Handling 

## Approach

Use two-pointer technique.
Use L to update the unique elemnts in the array, and R to access the current element. 
Check if the length of array is less than 2, if yes return length of array.
Else, initaialize L=R=2.
If nums[R]==nums[L-2], increment R.
Else, update nums[L]=nums[R] and increment L and R.
Return L

## Time Complexity

Overall = O(n)

## Space Complexity

O(1)

## Mistakes I Made

I compared nums[R]==nums[R-2]. Which was correct for most of the cases,but caused error in some cases
Didnot consider the less than 2 length of array case.


## Similar Questions

-Remove Duplicates from Sorted Array 
-Maximum Tastiness of Candy Basket
-House Robber IV
