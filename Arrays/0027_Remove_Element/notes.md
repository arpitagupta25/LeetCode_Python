# Remove Element

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
Else, if nums[k]==val , increment i.
Else, update nums[k]=nums[i] and increment i and k.
Return k

## Time Complexity

Overall = O(n)

## Space Complexity

O(1)

## Mistakes I Made

Didnot consider the empty array case.
Wrong updation of nums[k]=nums[i].


## Similar Questions

-Remove Duplicates from Sorted Array
-Remove Linked List Elements
-Move Zeroes
-Maximum Tastiness of Candy Basket
-House Robber IV
