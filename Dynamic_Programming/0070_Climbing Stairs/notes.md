# Climbing Stairs

## Difficulty

Easy

## Pattern

Dynamic Programming (Fibonacci)

## Concepts Used

- Dynamic Programming
- Recursion
- Memoization
- Tabulation
- Space Optimization

## Approach

To reach the nth stair, there are only two possible last moves:

- Climb 1 step from the (n-1)th stair.
- Climb 2 steps from the (n-2)th stair.

Hence,

```
ways(n) = ways(n-1) + ways(n-2)
```

This forms the Fibonacci sequence.

Initially, the recursive solution works correctly but recalculates the same subproblems multiple times, resulting in exponential time complexity.

To optimize this, store the computed values in a DP array (Memoization) or build the answer iteratively using Tabulation.

## Time Complexity

- Recursive Solution: **O(2ⁿ)**
- Memoization: **O(n)**
- Tabulation: **O(n)**
- Space Optimized DP: **O(n)**

## Space Complexity

- Recursive Solution: **O(n)** (Recursion Stack)
- Memoization: **O(n)**
- Tabulation: **O(n)**
- Space Optimized DP: **O(1)**

## Mistakes I Made

- Forgot to use `self` while making recursive calls (`self.climbStairs()`).
- Initially thought storing recursive results in local variables (`num1`, `num2`) would avoid repeated computations.
- Realized that local variables only store results for the current function call and do not prevent future recursive calls from recomputing the same values.
- Learned that Memoization requires a shared DP array that persists across recursive calls.

## Similar Questions

- Min Cost Climbing Stairs
- House Robber
- Fibonacci Number
- N-th Tribonacci Number
- Decode Ways
- House Robber II
