# First Unique Character in a String

## Difficulty

Easy

## Pattern

Frequency Counting / Hash Map / String Traversal

## Concepts Used

- String
- Frequency Counting
- Dictionary / Hash Map
- String Traversal
- Two Passes

## Approach

- First, check if the string is empty. If it is empty, return `-1`.
- Create a dictionary to store the frequency of each character in the string.
- Traverse the string once and update the frequency of every character.
- Traverse the string again from left to right.
- For each character, check its frequency in the dictionary.
- If the frequency is `1`, that character is the first non-repeating character, so return its index.
- If no character has a frequency of `1`, return `-1`.
- Using a dictionary avoids repeatedly scanning the entire string with `s.count()`.

## Time Complexity

- Overall: O(n)
- First traversal takes O(n) to count the frequencies.
- Second traversal takes O(n) to find the first unique character.
- Dictionary lookup takes approximately O(1).
- Therefore, O(n) + O(n) = O(n).

## Space Complexity

- Overall: O(k)
- The dictionary stores the frequency of each distinct character.
- `k` represents the number of distinct characters.
- In the worst case, `k = n`, so the space complexity can be O(n).

## Mistakes I Made

- Initially used:
  ```python
  if s[i] in s[i+1:]:
  ```

## Similar Question

- Sort Character by Frequency
- First Letter to appear twice
