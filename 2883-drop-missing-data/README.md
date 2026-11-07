<!-- leetcode-notes-sync:start -->
# 2883. Drop Missing Data

[Open on LeetCode](https://leetcode.com/problems/drop-missing-data/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191219282](https://leetcode.com/problems/drop-missing-data/submissions/2191219282/).

LeetCode 2883 — Drop Missing Data
Difficulty: Easy
Topic: Pandas, Data Cleaning

Intuition:
Remove rows where the name column has missing values.

Approach:
1. Use dropna() to remove missing values.
2. Set subset=["name"] to check only names.
3. Return the cleaned DataFrame.

Example:
Names: [Amit, None, Priya]
Output: [Amit, Priya]

Complexity:
Time: O(n)
Space: O(n)

Key Learnings:
- dropna() removes rows containing missing values.
- subset specifies which columns to check.
- None and NaN represent missing values.
- By default, dropna() returns a new DataFrame.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191219282](https://leetcode.com/problems/drop-missing-data/submissions/2191219282/) | 2026-11-07 10:51:01 | pythondata | [Source](submissions/2191219282.py) |
<!-- leetcode-notes-sync:end -->
