# Find the Index of the First Occurrence in a String

## Difficulty
Easy

## Pattern
String Matching

## Concepts Used

- String
- Brute Force
- Two Pointers (Index Traversal)

## Approach

Traverse the `haystack` string and consider each index as a possible starting position for the `needle`.

For every valid starting index:
- Compare the substring of length equal to `needle` with the `needle`.
- If they are equal, return the current index immediately.
- If no match is found after checking all possible positions, return `-1`.

The loop only runs until `len(haystack) - len(needle)` because any index beyond that cannot accommodate the entire `needle`.

## Time Complexity

**Overall:** `O((n - m + 1) × m)` ≈ **O(n × m)**

- `n` = Length of `haystack`
- `m` = Length of `needle`

In the worst case, every possible starting position is checked and up to `m` characters are compared each time.

## Space Complexity

**Overall:** `O(1)`

Only a few variables are used, so no extra space proportional to the input size is required.

## Mistakes I made

- iterating through every character of `haystack`, which can lead to unnecessary comparisons once there isn't enough space left for the `needle`.
- while Python provides the built-in `find()` method, implementing the search manually helps strengthen understanding of string traversal and is preferred in coding interviews.

## Similar Questions

- Shortest Palindrome
- Repeated Substring Pattern
