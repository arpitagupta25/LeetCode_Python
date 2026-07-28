## Isomorphic Strings

## Difficulty
Easy

## Pattern

Hash Table

## Concepts Used

-String
-Hash Map (Dictionary)

## Approach

First, check if both strings have the same length. If not, return False.
Use a dictionary to store the mapping from characters in s to characters in t.
Traverse both strings simultaneously.
If the current character from s is not already mapped:
Check whether the corresponding character in t is already mapped by another character.
If it is, return False.
Otherwise, create the new mapping.
If the current character from s is already mapped:
Verify that it maps to the current character in t.
If not, return False.
If all mappings remain consistent throughout the traversal, return True.

## Time Complexity

Overall: O(n²) (using t[i] in iso_dict.values() because checking values takes O(n) each time)

Note: This can be optimized to O(n) by maintaining another dictionary (or a set) for the reverse mapping.

## Space Complexity

Overall: O(n)

## Mistakes I Made

-Reversed the length check.
``` python 
if len(s) == len(t):
    return False
```
-It should return False only when the lengths are different.
-Checked only one-way mapping (s → t) and forgot to ensure that two different characters from s cannot map to the same character in t.
-Forgot to return False when a new character in s tried to map to an already-mapped character in t.
``` python 
if t[i] not in iso_dict.values():
    iso_dict[s[i]] = t[i]
```
-If t[i] is already present in iso_dict.values(), the code should immediately return False instead of silently continuing.

## Similar Questions

Isomorphic Strings
Word Pattern
Find and Replace Pattern
Group Anagrams
Valid Anagram
Jewels and Stones
Ransom Note
Word Subsets
