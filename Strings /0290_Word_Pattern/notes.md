# 290. Word Pattern

## Difficulty

Easy

## Pattern

Hash Map / Dictionary, Two-way Mapping, Bijection

## Concepts Used

- String
- Array
- Hash Map / Dictionary
- Two-way Mapping
- Bijection
- String Splitting

## Approach

The main idea is to treat this problem as a **mapping problem**.

We need a one-to-one relationship between:

```text
Character ↔ Word
```

-Split the string s into individual words using s.split() so that each character in pattern can be compared with one complete word.
-Check the lengths of pattern and words; if they are different, return False because every character must correspond to exactly one word.
-Use two dictionaries to maintain a two-way mapping: one for character → word and another for word → character, ensuring a one-to-one (bijection) relationship.
-Traverse the pattern and words together and check whether an existing character is mapped to a different word or an existing word is mapped to a different character; if either happens, return False.
-Store new mappings when both the character and word have not been mapped before.
-Return True after the complete traversal if no conflicting mapping is found.

## Time Complexity

O(n)

## Space Complexity

O(n)

## Mistakes I made

- I considered only one way mapping.
- Forgot to split the words.
- Returned True after checking the one side mapping.

## Similar Questions

- Isomorphic Strings
- Find and Replace Pattern 
