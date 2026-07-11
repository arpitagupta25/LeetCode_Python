# Container With Most Water

## Difficulty
Medium

## Pattern
Greedy Two-pointer concept

## Concepts Used

- Array
- Duplicate Handling 

## Approach

Use two-pointer technique to find the minimum among the two.
Using that, we find area (minimum among the two * width )
Checking if the resultant area is greater than the existing area.
If yes, updating area value.
If the left value is less than right, we incre,ent left value.
Else, we decrement right value.
Repeating while left<right.

## Time Complexity

Overall = O(n)

## Space Complexity

O(1)

## Mistakes I Made

Sorted the array.
Misunderstood with 3Sum question.
Incorrect pointer movement.


## Similar Questions

-Trapping Rain Water
-Maximum Tastiness of Candy Basket
-House Robber IV
