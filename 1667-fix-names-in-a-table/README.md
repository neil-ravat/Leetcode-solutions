<!-- leetcode-notes-sync:start -->
# 1667. Fix Names in a Table

[Open on LeetCode](https://leetcode.com/problems/fix-names-in-a-table/)

**Difficulty:** Easy

## My notes

### Submission notes

From accepted submission [#2192764168](https://leetcode.com/problems/fix-names-in-a-table/submissions/2192764168/).

LeetCode #1667 — Fix Names in a Table

Pattern: String Transformation + Sorting

Approach:
1. Apply .str.capitalize() to the name column.
2. Sort by user_id in ascending order.
3. Return the updated DataFrame.

Key Learning:
- .str applies string operations to each row.
- .str.capitalize() makes the first character uppercase
  and the remaining characters lowercase.
- .str.upper() and .str.lower() change the entire string.

Time: O(n log n) including sorting
Space: O(n) for transformed strings and sorting

## Accepted submissions

| Submission | Submitted (UTC) | Language | Code |
| --- | --- | --- | --- |
| [2192764168](https://leetcode.com/problems/fix-names-in-a-table/submissions/2192764168/) | 2026-11-09 21:06:26 | pythondata | [Source](submissions/2192764168.py) |
<!-- leetcode-notes-sync:end -->
