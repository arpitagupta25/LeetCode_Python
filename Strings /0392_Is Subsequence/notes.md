# Is Subsequence

## Difficulty

Easy

## Pattern

Two Pointers

## Approach

- Use two pointers: one pointer `i` for string `s` and scan string `t` using another pointer.
- Traverse through `t` character by character.
- If the current character of `t` matches `s[i]`, move `i` forward because we found the next required character of the subsequence.
- If the characters do not match, simply continue scanning `t`.
- At the end, if `i == len(s)`, all characters of `s` were found in the correct order, so return `True`.
- Otherwise, return `False.
- The key idea is that **the characters must appear in the same relative order**, not just exist somewhere in `t`.

## Time Complexity 

O(n)

## Space Complexity 

O(1)

## Mistakes I made 

-Used in instead of checking order.
-I used split() incorrectly.
Did not account for relative positions.

## Similar Questions

-Number of Matching Subsequences
-Append Characters to String to Make Subsequence
-Make String a Subsequence Using Cyclic Increments
