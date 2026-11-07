<!-- leetcode-notes-sync:start -->
# 2891. Method Chaining

[Open on LeetCode](https://leetcode.com/problems/method-chaining/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191235822](https://leetcode.com/problems/method-chaining/submissions/2191235822/).

LeetCode 2891 — Method Chaining
Difficulty: Easy
Topic: Pandas, Filtering, Sorting, Chaining

Intuition:
Find animals heavier than 100 kg and sort them
from heaviest to lightest.

Approach:
1. Filter rows where weight > 100.
2. Sort by weight with ascending=False.
3. Select only the name column.
4. Return the resulting DataFrame.

Example:
Weights: [220, 5, 3000, 30, 190]
Output: [Elephant, Tiger, Lion]

Complexity:
Time: O(n + k log k)
Space: O(n)
(n = total rows, k = matching rows)

Key Learnings:
- Boolean conditions filter rows.
- sort_values() sorts DataFrames.
- ascending=False means descending order.
- [["name"]] returns a DataFrame.
- Filtering before sorting can improve efficiency.
- Method chaining combines multiple operations.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191235822](https://leetcode.com/problems/method-chaining/submissions/2191235822/) | 2026-11-07 11:32:54 | pythondata | [Source](submissions/2191235822.py) |
<!-- leetcode-notes-sync:end -->
