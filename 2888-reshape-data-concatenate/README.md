<!-- leetcode-notes-sync:start -->
# 2888. Reshape Data: Concatenate

[Open on LeetCode](https://leetcode.com/problems/reshape-data-concatenate/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191227843](https://leetcode.com/problems/reshape-data-concatenate/submissions/2191227843/).

LeetCode 2888 — Reshape Data: Concatenate
Difficulty: Easy
Topic: Pandas, DataFrame Concatenation

Intuition:
Combine two DataFrames vertically into one.

Approach:
1. Use pd.concat([df1, df2]).
2. Set ignore_index=True to reset indexes.
3. Return the combined DataFrame.

Example:
df1: [A, B]
df2: [C, D]
Output: [A, B, C, D]

Complexity:
Time: O(n + m)
Space: O(n + m)
(n, m = rows in each DataFrame, with fixed columns)

Key Learnings:
- pd.concat() combines DataFrames.
- axis=0 stacks rows (default).
- ignore_index=True creates sequential indexes.
- Boolean True must not be written as "True".

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191227843](https://leetcode.com/problems/reshape-data-concatenate/submissions/2191227843/) | 2026-11-07 11:12:43 | pythondata | [Source](submissions/2191227843.py) |
<!-- leetcode-notes-sync:end -->
