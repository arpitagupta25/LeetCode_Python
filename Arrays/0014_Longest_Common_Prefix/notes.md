# Longest Common Prefix

## Difficulty

Easy

## Pattern

String, Prefix Matching

## Concepts Used

- String
- Prefix Comparison
- String Slicing
- Iteration

## Approach

Assume the first string is the common prefix.

Compare this prefix with every other string in the array.
If the current string does not start with the prefix, keep removing the last character from the prefix until it matches.
If the prefix becomes empty, return an empty string.
After comparing with all strings, return the remaining prefix.

## Time Complexity

- Worst Case: O(n × m)

Where:
- n = Number of strings
- m = Length of the shortest string

## Space Complexity

O(1)

## Mistakes I Made

- Forgot to handle the case when the input array is empty.
- Initially tried comparing every pair of strings instead of maintaining a common prefix.
- Forgot to return immediately when the prefix became empty.

## Similar Questions

- Smallest Missing Integer Greater Than Sequential Prefix Sum
- Longest Common Suffix Queries
- Find the Length of the Longest Common Prefix
- Shortest Common Supersequence
- Implement `strStr()`
- Find the Index of the First Occurrence in a String
