## Valid Palindrome

## Difficulty

Easy

## Pattern

String

## Concepts Used

String
Two Pointers
Regular Expressions (re)
String Manipulation

## Approach

Convert the entire string to lowercase so that uppercase and lowercase letters are treated the same.
Remove all non-alphanumeric characters (spaces, punctuation, symbols) using a regular expression.
Reverse the cleaned string.
Compare the reversed string with the cleaned string.
If both are equal, return True; otherwise, return False.
Note: Although this solution reverses the string, the optimal approach is to use two pointers from both ends without creating a reversed string.

## Time Complexity

Overall: O(n)

## Space Complexity

Overall: O(n)

## Mistakes I Made

Used an extra string (rev) to reverse the input instead of using the optimal two-pointer approach.
Created a new reversed string character by character:
``` python
rev = ""
for i in range(len(s)-1, -1, -1):
    rev += s[i]
```
String concatenation inside a loop is less efficient because strings are immutable in Python.
Initially focused on reversing the string instead of comparing characters from both ends.
Relied on re.sub() without considering that the problem can also be solved without regular expressions using isalnum().
Used additional space for the reversed string, whereas the optimal solution uses O(1) extra space.

## Similar Questions

Palindrome Linked List
Maximum Product of the Length of Two Palindromic Subsequences
Find First Palindromic String in the Array
Valid Palindrome II
Maximum Palindromes After Operations
Palindrome Number
Two Sum II – Input Array Is Sorted
Reverse Vowels of a String
