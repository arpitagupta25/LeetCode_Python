# Total 3-Digit Even Numbers

## Difficulty

Easy

## Pattern

Brute Force / Enumeration / Hash Set

## Concepts Used

- Arrays
- Nested Loops
- Index Tracking
- Even Numbers
- Sets
- Duplicate Handling

## Approach

- We need to form a 3-digit even number using the given digits.
- Use three loops to represent the three positions of the number:
  - `i` → last digit
  - `j` → first digit
  - `k` → middle digit
- The last digit must be even, so check `digits[i] % 2 == 0`.
- The same array element cannot be reused, so make sure `i`, `j`, and `k` are different.
- The first digit cannot be `0`, because then the number would not be a 3-digit number.
- Construct the number using the actual digit values at those indices:
  - First digit → `digits[j]`
  - Middle digit → `digits[k]`
  - Last digit → `digits[i]`
- Store every valid number in a `set`.
- Using a set ensures that duplicate numbers are counted only once, even when the input contains repeated digits such as `[6,6,6]` or `[0,2,2]`.
- Finally, return the size of the set.

## Time Complexity

**O(n³)**

- Three nested loops are used.
- Each loop can run up to `n` times.
- Therefore, the overall time complexity is `O(n³)`.

Since the problem has at most a small number of digits, this brute-force approach is efficient.

## Space Complexity

**O(k)**

- `k` is the number of distinct valid 3-digit numbers stored in the set.
- Since there are only finitely many possible 3-digit numbers, the extra space is bounded.

## Mistakes I Made

- Initially tried to use `remove()` to create the remaining digits.
- Forgot that `list.remove()` modifies the original list and does not return the modified list.
- Used `temp = digits`, which creates another reference to the same list instead of a copy.
- Initially tried to handle duplicates using `len(digits) == len(set(digits))`.
- Realized that duplicate digits do not necessarily make a number invalid; they can still be used if they occur at different indices.
- Initially used the indices `i`, `j`, and `k` while constructing the number instead of the actual digit values `digits[i]`, `digits[j]`, and `digits[k]`.
- Realized that using a `set` is a simple way to avoid counting the same number multiple times when duplicate digits are present.

## Similar Questions

- Finding 3-Digit even number
