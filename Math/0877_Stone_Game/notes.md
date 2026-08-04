## Stone Game

## Difficulty

Medium

## Pattern

Game Theory / Mathematical Observation

## Concepts Used

Array
Game Theory
Greedy Observation
Optimal Play
Mathematical Proof

## Approach

This problem looks like a Dynamic Programming problem, but because of the given constraints, it has a simple mathematical solution.

Alice always makes the first move.
There are an even number of piles.
The total number of stones is odd, so a tie is impossible.
Alice can choose to collect either all even-indexed piles or all odd-indexed piles.
Before making her first move, Alice compares the total stones in the even-indexed piles and odd-indexed piles.
She commits to collecting the group (even or odd) with the larger total.
Since Alice moves first, she can always force Bob to leave her the desired parity of piles.
Therefore, Alice is guaranteed to collect more stones than Bob.
Hence, simply return True.

## Time Complexity

Overall = O(1)

## Space Complexity

O(1)

## Mistakes I Made

Initially tried to simulate every possible move made by Alice and Bob.
Assumed Alice must always choose the leftmost pile first.
Forgot that both players play optimally, so Alice always chooses the move that guarantees victory.
Tried to solve the problem using recursion/DP without noticing the mathematical observation.
Didn't realize that Alice can always force herself to take either all even-indexed or all odd-indexed piles.
Missed the significance of the constraints:
Even number of piles.
Odd total number of stones (no tie possible).

## Similar Questions

Stone Game V
Stone Game VI
Strictly Palindromic Number
Visit Array Positions to Maximize Score
Can I Win
Nim Game
Divisor Game
