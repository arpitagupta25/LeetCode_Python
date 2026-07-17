# Merge Sorted Array

## Difficulty

Easy

## Pattern

Two-pointer concept

## Concepts Used

- Array
- Two-pointer
- In-place merging
- Sorting

## Approach

Use two pointers to traverse both arrays simultaneously.

- If `m == 0`, copy all elements of `nums2` into `nums1` and return.
- If `n == 0`, no merging is required, so return.
- Initialize two pointers:
  - `i = 0` for `nums1`
  - `j = 0` for `nums2`
- Compare `nums1[i]` and `nums2[j]`.
- Append the smaller element to a temporary array `temp` and move the corresponding pointer.
- Once one array is completely traversed, append the remaining valid elements from the other array:
  - Remaining elements of `nums1` are from `nums1[i:m]`.
  - Remaining elements of `nums2` are from `nums2[j:n]`.
- Finally, copy the contents of `temp` back into `nums1`.

## Time Complexity

Overall = O(m + n)

## Space Complexity

O(1)

## Mistakes I Made

- Returned immediately when `m == 0`, without copying the elements of `nums2` into `nums1`.
- While copying the remaining elements of `nums1` in my temporary-array approach, I mistakenly used:
  ```python
  nums1[i:n]
  ```
  instead of:
  ```python
  nums1[i:m]
  ```
  Since only the first `m` elements in `nums1` are valid, using `n` resulted in incorrect slicing.
- Forgot that the extra zeros at the end of `nums1` are placeholders and should not be treated as valid elements.
- Initially solved the problem using an auxiliary array (`temp`), which uses **O(m + n)** extra space instead of the expected **O(1)** in-place approach.

## Similar Questions

- Merge Two Sorted Lists
- Square of sorted Array
- Interval List Interactions
- Table K of each character from left to right
