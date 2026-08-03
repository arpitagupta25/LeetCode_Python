# Majority Element

## Difficulty

Easy

## Pattern

Boyer-Moore Voting Algorithm / Hash Table

## Concepts Used

- Array
- Hash Map (Dictionary)
- Boyer-Moore Voting Algorithm
- Frequency Counting

## Approach

### Hash Map Approach

Traverse the array once while maintaining a dictionary to store the frequency of each element.

- If the current element is not present in the dictionary, initialize its count as 1.
- Otherwise, increment its existing count.
- After updating the count, check whether it is greater than `len(nums) // 2`.
- If it is, return that element immediately.

### Optimal Approach (Boyer-Moore Voting Algorithm)

Maintain two variables: `candidate` and `count`.

- If `count` becomes 0, choose the current element as the new candidate.
- If the current element is the same as the candidate, increment `count`.
- Otherwise, decrement `count`.
- Since the majority element appears more than half of the time, it cannot be completely cancelled by other elements and will remain as the final candidate.

## Time Complexity

### Hash Map Approach

Overall = **O(n)**

### Boyer-Moore Voting Algorithm

Overall = **O(n)**

## Space Complexity

### Hash Map Approach

**O(n)**

### Boyer-Moore Voting Algorithm

**O(1)**

## Mistakes I Made

- Used `nums.count()` inside a loop, resulting in **O(n²)** time complexity.
- Checked `if i not in dict_cnt` instead of `if nums[i] not in dict_cnt`.
- Used a single `cnt` variable for all elements instead of updating each element's count in the dictionary.
- Forgot that the dictionary already stores the previous frequency, so the count should be incremented using `dict_cnt[nums[i]] += 1`.

## Similar Questions

- Majority Element II
- Most Frequent Even Element
- Minimum Operations to Exceed Threshold Value I
- Sort Characters By Frequency
- Find the Difference
- Majority Element II
