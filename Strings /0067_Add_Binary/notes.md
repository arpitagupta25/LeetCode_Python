# Add Binary

## Difficulty

Easy

## Pattern

Simulation / String Traversal

## Concepts Used

- String
- Binary Addition
- Carry
- Two Pointers / Index Traversal
- Dictionary

## Approach

- Start from the rightmost characters of both binary strings.
- Use two pointers, `i` and `j`, to traverse both strings from right to left.
- Maintain a `carry` for the previous binary addition.
- For every position, consider:
  - Current digit from `a`
  - Current digit from `b`
  - Current `carry`
- Use a dictionary to determine the resulting carry and binary digit for the three-bit combination.
- Add the resulting digit to the beginning of `final_ans`.
- If one string is shorter, treat its missing digits as `0` and continue processing the remaining digits.
- After both strings are processed, add the final carry only if it is `1`.
- Return the resulting binary string.

## Time Complexity

- Overall: O(n)
- Where `n = max(len(a), len(b))`
- Each digit is processed once.

## Space Complexity

- Overall: O(n)
- `final_ans` stores the resulting binary string.
- The dictionary contains only a constant number of entries, so it contributes O(1) auxiliary space.

## Mistakes I Made

- Initially converted the binary strings directly into integers using:
  ```python
int_a = int(a, 2)
int_b = int(b, 2)
```
- Added the carry to final answer even if the carry was 0.
-Stored the keys of dictionary as a list.

## Similar Questions

-Multiply Strings
-Add Two Numbers
-Add to array-form of integer

```python
int_a = int(a, 2)
int_b = int(b, 2)
