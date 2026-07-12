# Trapping Rain Water

## Difficulty
Hard

## Pattern
Two-pointer concept

## Concepts Used

- Array
- Two pointer concept 

## Approach

We compare the heights at the two pointers.
If height[left] < height[right] ( water level on the left is determined solely by left_max.) , then If the current left bar is taller than or equal to left_max, update left_max.
Otherwise, water is trapped: left_max - height[left]
Move the left pointer one step to the right.
If height[right] <= height[left] ( water level on the left is determined solely by right_max.) , then If current right bar is taller than or equal to right_max, update right_max.
Otherwise, water trapped is: right_max - height[right]
Move the right pointer one step to the left.

## Time Complexity

Overall = O(n)

## Space Complexity

O(1)

## Mistakes I Made

Calculated the water trapping formula wrong. 
Only considered non-zero bars.

## Similar Questions

- Container With Most Water
- Product of Array Except Self
- Trapping Rain Water II
- Maximum Value of an Ordered Triplet II
- Three Sum
