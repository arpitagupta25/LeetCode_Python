# Maximum Subarray

## Difficulty

Medium

## Pattern

Greedy (Kadane's Algorithm)

## Concepts Used

- Array
- Greedy
- Dynamic Programming (Kadane's Algorithm)

## Approach

Maintain two variables:

- `current_sum` → Maximum subarray sum ending at the current index.
- `max_sum` → Maximum subarray sum found so far.

For each element:
- Start a new subarray or extend the existing one.
- Update `max_sum` if `current_sum` becomes larger.

Return `max_sum`.

## Time Complexity

- **O(n)**
  
## Space Complexity

- **O(1)** 

## Mistakes I Made

- Initially used nested loops, resulting in **O(n²)** time complexity.
- Did not recognize that if the running sum becomes negative, it should be discarded.
- Focused on checking every possible subarray instead of making a greedy decision at each index.
- Didn't identify the pattern as **Kadane's Algorithm**, which is the optimal solution.
- Overlooked that the maximum subarray can consist of a single element (especially when all elements are negative).

## Similar Questions

- Best Time to Buy and Sell Stock
- Maximum Product Subarray
- Degree of an Array
- Longest Turbulent Subarray
- Maximum Score Of Spliced Array
