# Best Time to Buy and Sell Stock

## Difficulty
Easy

## Pattern
Single Pass / Greedy

## Concepts Used

- Array
- Greedy
- Single Pass Traversal
- Running Minimum

## Approach

Traverse the array once while maintaining the **minimum stock price** seen so far.
For each day's price:
- Update the minimum buying price if the current price is lower.
- Calculate the profit if the stock were sold on the current day.
- Update the maximum profit whenever a larger profit is found.
Since the buying day must always come before the selling day, tracking the minimum price encountered during traversal ensures that every profit calculation is valid.

## Time Complexity:

Overall: O(n)
  
## Space Complexity:

O(1)

## Mistakes I made

-Choosing the Global Minimum Price
-Using `index()` with Duplicate Minimum Values

## Similar Questions

-Maximum Subarray
-Best Time to Buy and Sell Stock II
-Best Time to Buy and Sell Stock III
-Best Time to Buy and Sell Stock IV
-Best Time to Buy and Sell Stock with Cooldown
-Sum of Beauty in the Array
-Maximum Difference Between Increasing Elements
-Best Time to Buy and Sell Stock V
