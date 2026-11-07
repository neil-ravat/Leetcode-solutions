<!-- leetcode-notes-sync:start -->
# 2886. Change Data Type

[Open on LeetCode](https://leetcode.com/problems/change-data-type/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2191225706](https://leetcode.com/problems/change-data-type/submissions/2191225706/).

LeetCode 2886 — Change Data Type
Difficulty: Easy
Topic: Pandas, Data Type Conversion

Intuition:
Convert the grade column from float to integer.

Approach:
1. Access the grade column.
2. Use astype(int) to convert its values.
3. Assign the converted values back.
4. Return the updated DataFrame.

Example:
Input:  [73.0, 87.0]
Output: [73, 87]

Complexity:
Time: O(n)
Space: O(n) for converted values.

Key Learnings:
- astype() converts column data types.
- astype(int) converts values to integers.
- Assign the result back to update the column.
- Converting decimals to int truncates them.

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2191225706](https://leetcode.com/problems/change-data-type/submissions/2191225706/) | 2026-11-07 11:07:26 | pythondata | [Source](submissions/2191225706.py) |
<!-- leetcode-notes-sync:end -->
