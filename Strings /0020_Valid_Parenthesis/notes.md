# Valid Parenthesis

## Difficulty

Easy

## Pattern

Stack

## Concepts Used

- String
- Stack

## Approach

- Use a stack of characters.
- When you encounter an opening bracket, push it to the top of the stack.
- When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false. Expand outward while the characters match.

## Time Complexity

- Overall: O(n)

## Space Complexity

- Overall: O(1)

## Mistakes I Made

-Trying to compare different characters. As, Opening and closing brackets are different characters

 ```python
stk[-1] == i
```

- Tries to remove a closing bracket that's never stored
```python
stk.remove(i)
```

## Similar Questions

- Generate Parentheses
- Longest Valid Parentheses
- Remove Invalid Parentheses
- Check If Word Is Valid After Substitutions
- Check if a Parentheses String Can Be Valid
- Move Pieces to Obtain a String
- **131. Palindrome Partitioning**
- **132. Palindrome Partitioning II**
