# Reverse String

## Difficulty

Easy

## Pattern

String

## Concepts Used

- String
- Two pointer 

## Approach

Reverse the string **in-place** by swapping characters from the beginning and end of the list.

- Find the length of the string and store it in `n`.
- Loop through the first half of the list using `range(n//2)`.
- For every position `i`:
  - Store `s[i]` temporarily.
  - Replace `s[i]` with the character at the current end (`s[n-1]`).
  - Replace `s[n-1]` with the stored character.
- After every swap, decrease `n` by `1` so that the next swap happens with the next character from the right.
- Since only the first half needs to be processed, all characters are reversed after `n//2` swaps.
- The reversal is done **in-place**, meaning no extra list is created.

## Time Complexity

- Overall: O(n)

## Space Complexity

- Overall: O(1)

## Similar Questions

- Reverse Vowels of a String
- Reverse String II
- **131. Palindrome Partitioning**
- **132. Palindrome Partitioning II**
