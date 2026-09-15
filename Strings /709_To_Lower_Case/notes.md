# To Lower Case

## Difficulty

Easy

## Pattern

ASCII characters

## Concepts Used

- String

## Approach

- Convert the string into list.
- Iterate through each character of list.
- If their ASCII character lies between 65 to 97, then add 32 to it.
  ``` python
  result_ord=ord(lst_s[i])+32
  ```
- Later convert the list into string.
  ``` python
  "".join(lst_s)
  ```
- Return the resultant string.


## Time Complexity

- Overall: O(n)

## Space Complexity

- Overall: O(1)

## Mistakes I Made

- Converted the list into string using str() function.

## Similar Questions

- Capitalize the title
