# Longest Palindromic Substring

## Difficulty

Medium

## Pattern

Expand Around Center

## Concepts Used

- String
- Two Pointers
- Expand Around Center

## Approach

- Treat every index as the center of an **odd-length palindrome**.
- Treat every adjacent pair of indices as the center of an **even-length palindrome**.
- Expand outward while the characters match.
- Track and update the longest palindrome found.
- Return the longest palindrome.


## Time Complexity

- Overall: O(n²)

## Space Complexity

- Overall: O(1)

## Mistakes I Made

- Assumed the longest palindrome is centered in the middle of the string.
- Checked only one center instead of every possible center.
- Missed handling both odd and even palindromes for every index.
- Infinite loop when characters didn't match.
- Returned incorrect substring boundaries after expansion.
- Didn't keep track of the longest palindrome found.

## Key Takeaways

- Every character can be the center of a palindrome.
- Every gap between two characters can also be a center.
- Expand while characters match.
- Update the longest palindrome after every expansion.

## Similar Questions

- Longest Palindromic Subsequence
- Shortest Palindrome
- Palindrome Pairs
- **131. Palindrome Partitioning**
- **132. Palindrome Partitioning II**
