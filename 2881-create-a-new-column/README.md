<!-- leetcode-notes-sync:start -->
# 2881. Create a New Column

[Open on LeetCode](https://leetcode.com/problems/create-a-new-column/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191173107](https://leetcode.com/problems/create-a-new-column/submissions/2191173107/).

LeetCode 2881 — Create a New Column
Difficulty: Easy
Topic: Pandas, Column Transformation

Intuition:
Create a bonus column containing twice the salary.

Approach:
1. Access the salary column.
2. Multiply each value by 2.
3. Store the result in a new bonus column.
4. Return the updated DataFrame.

Example:
Salary: [5000, 7000]
Bonus:  [10000, 14000]

Complexity:
Time: O(n)
Space: O(n) for the new column.

Key Learnings:
- df["new"] creates or updates a column.
- Arithmetic works directly on entire columns.
- Pandas uses vectorized operations.
- No explicit loops are required.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191173107](https://leetcode.com/problems/create-a-new-column/submissions/2191173107/) | 2026-11-07 08:54:03 | pythondata | [Source](submissions/2191173107.py) |
<!-- leetcode-notes-sync:end -->
