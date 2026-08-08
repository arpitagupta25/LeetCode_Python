# Fizz Buzz

## Difficulty

Easy

## Pattern

Simulation / Conditional Logic

## Concepts Used

- Array / List
- Loop
- Conditional Statements
- Modulo Operator (`%`)
- String Conversion

## Approach

Iterate through all numbers from `1` to `n` and determine what string should be added to the answer list.

For each number `i`:

1. If `i` is divisible by both `3` and `5`, append `"FizzBuzz"`.
2. Else if `i` is divisible by `3`, append `"Fizz"`.
3. Else if `i` is divisible by `5`, append `"Buzz"`.
4. Otherwise, append `i` as a string.

The modulo operator `%` is used to check whether a number is divisible by another number.

### Example

For `n = 5`:

```text
1 → "1"
2 → "2"
3 → "Fizz"
4 → "4"
5 → "Buzz"
