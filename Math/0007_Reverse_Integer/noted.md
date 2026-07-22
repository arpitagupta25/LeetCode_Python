# Reverse Integer

## Difficulty

Medium

## Pattern

Math / Digit Manipulation

## Concepts Used

- Math
- Modulo (`%`)
- Integer Division (`//`)
- Integer Manipulation
- Overflow Handling (32-bit Signed Integer)

## Approach

Reverse the digits of the integer one by one using modulo and integer division.

- Determine whether the number is positive or negative.
- Work with the absolute value of the number.
- Initialize `rev = 0`.
- While the number is greater than `0`:
  - Extract the last digit using `x % 10`.
  - Append the digit to the reversed number:
    ```python
    rev = rev * 10 + rem
    ```
  - Remove the last digit using:
    ```python
    x //= 10
    ```
- Restore the original sign of the reversed number.
- Check whether the reversed integer lies within the 32-bit signed integer range:
  - `-2^31 <= rev <= 2^31 - 1`
- If it is outside the range, return `0`; otherwise, return the reversed integer.

## Time Complexity

Overall = **O(log₁₀ n)**

## Space Complexity

**O(1)**

## Mistakes I Made

- Tried checking overflow using:
  ```python
  x.bit_length()
  ```
  instead of verifying whether the **reversed integer** is within the 32-bit signed integer range.
- Used an undefined variable:
  ```python
  signed
  ```
  while determining the bit limit.
- Initially reversed the number by converting it into a string, which increases space complexity unnecessarily.
- Forgot to handle the special case when `x == 0`.
- Checked for overflow before reversing the integer instead of after obtaining the reversed value.

## Similar Questions

- String to Integer (atoi)
- Reverse Bits
- A Number After a Double Reversal
- Count Number of Distinct Integers After Reverse Operations
- Integer to Roman
- Roman to Integer
- String to Integer (atoi)
