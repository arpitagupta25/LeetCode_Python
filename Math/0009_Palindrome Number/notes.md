# Palindrome Number

## Difficulty

Easy

## Pattern

Math / Digit Manipulation

## Concepts Used

- Math
- Modulo (`%`)
- Integer Division (`//`)
- Integer Reversal
- Number Comparison

## Approach

Reverse the given integer mathematically and compare it with the original number.

- Negative numbers can never be palindromes because of the `-` sign.
- Store the original number in a separate variable.
- Initialize `rev = 0`.
- While the number is greater than `0`:
  - Extract the last digit using:
    ```python
    rem = x % 10
    ```
  - Append the digit to the reversed number:
    ```python
    rev = rev * 10 + rem
    ```
  - Remove the last digit:
    ```python
    x //= 10
    ```
- Compare the reversed number with the original number.
- If both are equal, return `True`; otherwise, return `False`.

## Time Complexity

Overall = **O(log₁₀ n)**

## Space Complexity

**O(1)**

## Mistakes I Made

- Initialized the reversed number as:
  ```python
  rev = 1
  ```
  instead of:
  ```python
  rev = 0
  ```
  which produced an incorrect reversed value.

- Forgot to explicitly handle negative numbers.
  ```python
  if x < 0:
      return False
  ```
  Negative integers are never palindromes because the minus sign appears only on one side.

- Initially assumed the loop condition
  ```python
  while x > 0
  ```
  was sufficient for all cases, but it skips negative numbers entirely. Although it returns the correct result for negatives, handling them explicitly makes the solution clearer.

- Compared against the original number without ensuring the reversed number was constructed correctly due to the incorrect initialization of `rev`.

## Similar Questions

- Palindrome Linked List
- Strictly Palindromic Number
- Find Palindrome With Fixed Length
- Find the Count of Good Integers
- Reverse Bits
- A Number After a Double Reversal
- Count Number of Distinct Integers After Reverse Operations
