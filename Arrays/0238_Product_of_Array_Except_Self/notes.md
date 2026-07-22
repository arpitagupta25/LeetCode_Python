# Product of Array Except Self

## Difficulty

Medium

## Pattern

Prefix & Suffix Products

## Concepts Used

- Array
- Prefix Product
- Suffix Product
- In-place Computation
- Space Optimization

## Approach

Use the output array to store the prefix products of each element.

- Initialize an answer array with all elements as `1`.
- Traverse from left to right while maintaining a `prefix` product.
- Store the current `prefix` in `answer[i]` before updating it.
- Traverse from right to left while maintaining a `suffix` product.
- Multiply `answer[i]` with the current `suffix`.
- Update the `suffix` by multiplying it with the current element.
- Return the `answer` array.

This ensures each index contains the product of all elements to its left and right, excluding itself.

## Time Complexity

**O(n)**

## Space Complexity

**O(1)**

## Similar Questions

- Trapping Rain Water
- Maximum Product Subarray
- Construct Product Matrix
- 42. Trapping Rain Water
- 11. Container With Most Water
- 560. Subarray Sum Equals K
