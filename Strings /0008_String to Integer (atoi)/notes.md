# String to Integer (atoi)

## Difficulty
Medium

## Pattern
String Parsing

## Concepts Used

- String
- Two Pointers (Index Traversal)
- Integer Overflow Handling

## Approach

- Remove the leading whitespaces using `strip()`.
- Check if the string is empty. If yes, return `0`.
- Determine the sign by checking for `'+'` or `'-'`.
- Skip any leading zeros after the optional sign.
- Traverse the string character by character and collect consecutive digits.
- Stop parsing as soon as a non-digit character is encountered.
- If no digits were collected, return `0`.
- Convert the collected digits into an integer and apply the sign.
- If the integer exceeds the 32-bit signed integer range, clamp it to:
  - `-2^31` for underflow.
  - `2^31 - 1` for overflow.
- Return the final integer.

## Time Complexity

- Overall: **O(n)**

## Space Complexity

- Overall: **O(n)** (Since the digits are stored in a string before conversion.)

## Mistakes I Made

- Used `=` instead of `==` while checking for an empty string.
- Used the invalid method `isnum()` instead of `isdigit()`/`isnumeric()`.
- Tried to compare a character with `s.isnumeric()` instead of checking `s[index].isdigit()`.
- Assumed `lstrip()` modifies the original string, whereas it returns a new string.
- Forgot to move the pointer after processing the optional sign.
- Used `lstrip('0')` to skip leading zeros, which fails when a sign (`+` or `-`) is present.
- Initialized `num` with a space (`" "`) instead of an empty string (`""`).
- Didn't handle cases where the input contains only a sign (`"+"` or `"-"`).
- Continued parsing after invalid characters instead of stopping at the first non-digit.
- Converted the string to an integer multiple times instead of converting it once after parsing.

## Similar Questions

- Reverse Integer
- Palindrome Number
- Roman to Integer
- Integer to Roman
- Basic Calculator
- Basic Calculator II
- Decode String
- Valid Number
```
