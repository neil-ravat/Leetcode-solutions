<!-- leetcode-notes-sync:start -->
# 2884. Modify Columns

[Open on LeetCode](https://leetcode.com/problems/modify-columns/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191222003](https://leetcode.com/problems/modify-columns/submissions/2191222003/).

LeetCode 2884 — Modify Columns
Difficulty: Easy
Topic: Pandas, Column Modification

Intuition:
Double every employee's salary.

Approach:
1. Access the salary column.
2. Multiply its values by 2.
3. Assign the result back to the same column.
4. Return the updated DataFrame.

Example:
Salary: [5000, 7000]
Output: [10000, 14000]

Complexity:
Time: O(n)
Space: O(n) for calculated values.

Key Learnings:
- df["col"] accesses an existing column.
- Assigning to the same column updates its values.
- Pandas supports vectorized arithmetic.
- No explicit loops are needed.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191222003](https://leetcode.com/problems/modify-columns/submissions/2191222003/) | 2026-11-07 10:58:01 | pythondata | [Source](submissions/2191222003.py) |
<!-- leetcode-notes-sync:end -->
