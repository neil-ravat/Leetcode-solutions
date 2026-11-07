<!-- leetcode-notes-sync:start -->
# 2879. Display the First Three Rows

[Open on LeetCode](https://leetcode.com/problems/display-the-first-three-rows/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191170392](https://leetcode.com/problems/display-the-first-three-rows/submissions/2191170392/).

LeetCode 2879 — Display the First Three Rows
Difficulty: Easy
Topic: Pandas, Row Selection

Intuition:
Retrieve the first 3 rows of a DataFrame.

Approach:
1. Use .head(3) to select the first 3 rows.
2. Return the resulting DataFrame.

Example:
Input: DataFrame with 6 rows
Output: First 3 rows with all columns.

Complexity:
Time: O(1)
Space: O(1) for a fixed 3-row result.

Key Learnings:
- .head(n) returns the first n rows.
- .head() returns 5 rows by default.
- Original column order is preserved.
- No loops or extra DataFrame creation needed.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191170392](https://leetcode.com/problems/display-the-first-three-rows/submissions/2191170392/) | 2026-11-07 08:46:57 | pythondata | [Source](submissions/2191170392.py) |
<!-- leetcode-notes-sync:end -->
